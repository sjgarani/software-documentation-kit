#!/usr/bin/env python3
"""List, validate, and update statuses in project documentation."""

from __future__ import annotations

import argparse
from datetime import date
import getpass
import re
import sys
from pathlib import Path

ADR_STATES = ("Proposed", "Accepted", "Rejected", "Superseded", "Withdrawn")
SPEC_STATES = ("Draft", "In Review", "Approved", "In Progress", "Completed", "Cancelled")
RUNBOOK_STATES = ("Draft", "In Review", "Active", "Retired")
GUIDE_STATES = ("Draft", "In Review", "Published", "Retired")
TRANSITIONS = {
    "adr": {
        "Proposed": {"Accepted", "Rejected"},
        "Accepted": {"Superseded", "Withdrawn"},
        "Rejected": set(), "Superseded": set(), "Withdrawn": set(),
    },
    "spec": {
        "Draft": {"In Review", "Cancelled"},
        "In Review": {"Draft", "Approved", "Cancelled"},
        "Approved": {"In Progress", "Cancelled"},
        "In Progress": {"Completed", "Cancelled"},
        "Completed": set(), "Cancelled": set(),
    },
    "runbook": {
        "Draft": {"In Review"},
        "In Review": {"Draft", "Active", "Retired"},
        "Active": {"In Review", "Retired"},
        "Retired": set(),
    },
    "guide": {
        "Draft": {"In Review"},
        "In Review": {"Draft", "Published", "Retired"},
        "Published": {"In Review", "Retired"},
        "Retired": set(),
    },
}
STATUS_LINE = re.compile(r"(?m)^- \*\*Status:\*\*\s*(.*?)\s*$")
HISTORY_HEADING = re.compile(r"(?m)^## History\s*$", re.IGNORECASE)
HISTORY_TABLE = "| Date | Change | Owner |\n|---|---|---|"


def documentation_root(root: Path) -> Path:
    installed_docs = root / "docs"
    if (installed_docs / "adr").is_dir() or (installed_docs / "specs").is_dir():
        return installed_docs
    return root


def documents(root: Path):
    docs_root = documentation_root(root)
    for kind, folder, pattern, valid in (
        ("adr", "adr", "[0-9][0-9][0-9][0-9]-*.md", ADR_STATES),
        ("spec", "specs", "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*.md", SPEC_STATES),
        ("runbook", "runbooks", "runbook-*.md", RUNBOOK_STATES),
        ("guide", "guides", "*.md", GUIDE_STATES),
    ):
        directory = docs_root / folder
        if directory.is_dir():
            for path in sorted(directory.glob(pattern)):
                if kind == "runbook" and path.name == "runbook-template.md":
                    continue
                yield kind, path, valid


def read_state(path: Path) -> tuple[str | None, str | None]:
    matches = STATUS_LINE.findall(path.read_text(encoding="utf-8"))
    if len(matches) != 1:
        return None, f"expected exactly one Status field; found {len(matches)}"
    return matches[0], None


def append_history(content: str, change: str, owner: str) -> str:
    """Append one dated entry to the document's final History section."""
    change = " ".join(change.replace("|", "\\|").split())
    owner = " ".join(owner.replace("|", "\\|").split())
    entry = f"| {date.today().isoformat()} | {change} | {owner} |"
    placeholder = "| YYYY-MM-DD | Initial draft | Name |"
    if placeholder in content:
        return content.replace(placeholder, entry, 1)
    if not content.endswith("\n"):
        content += "\n"

    matches = list(HISTORY_HEADING.finditer(content))
    if not matches:
        return f"{content}\n## History\n\n{HISTORY_TABLE}\n{entry}\n"
    if len(matches) > 1:
        raise ValueError("document must contain only one History section")

    section_start = matches[0].end()
    section = content[section_start:]
    if HISTORY_TABLE not in section:
        content += f"\n{HISTORY_TABLE}\n{entry}\n"
        return content
    return f"{content.rstrip()}\n{entry}\n"


def command_list(root: Path, selected_kind: str | None = None) -> int:
    grouped = {kind: [] for kind in ("adr", "spec", "runbook", "guide")}
    for kind, path, valid in documents(root):
        if selected_kind and kind != selected_kind:
            continue
        state, error = read_state(path)
        grouped[kind].append((path, state, error or (None if state in valid else f"unknown status: {state!r}")))

    if not any(grouped.values()):
        description = {
            "adr": "numbered ADR", "spec": "dated Spec", "runbook": "tracked Runbook",
            "guide": "Guide",
        }.get(selected_kind, "tracked document")
        print(f"No {description} found.")
        return 0

    for kind, entries in grouped.items():
        if not entries:
            continue
        states = {
            "adr": ADR_STATES, "spec": SPEC_STATES, "runbook": RUNBOOK_STATES,
            "guide": GUIDE_STATES,
        }[kind]
        print(f"{kind.upper()} board")
        print("| Document | " + " | ".join(states) + " | Invalid |")
        print("|---|" + "|".join("---:" for _ in states) + "|---:|")
        for path, current, error in entries:
            marks = ["●" if current == state else "" for state in states]
            invalid_mark = "⚠" if error else ""
            print(f"| `{path.relative_to(root)}` | " + " | ".join(marks) + f" | {invalid_mark} |")
        invalid_entries = [(path, error) for path, _, error in entries if error]
        for path, error in invalid_entries:
            print(f"  - Invalid status in `{path.relative_to(root)}`: {error}")
        print()
    return 0


def command_check(root: Path) -> int:
    errors = []
    for kind, path, valid in documents(root):
        state, error = read_state(path)
        if error:
            errors.append(f"{path}: {error}")
        elif state not in valid:
            errors.append(f"{path}: unknown status: {state!r}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Statuses are valid.")
    return 0


def command_set(root: Path, relative: str, new_state: str, owner: str, change: str | None = None) -> int:
    path = (root / relative).resolve()
    docs_root = documentation_root(root).resolve()
    try:
        path.relative_to(docs_root)
    except ValueError:
        print("The document must be inside the documentation directory.", file=sys.stderr)
        return 2
    records = {item[1].resolve(): item for item in documents(root)}
    record = records.get(path)
    if record is None:
        print("Unrecognized or untracked document type.", file=sys.stderr)
        return 2
    kind, _, valid = record
    if new_state not in valid:
        print(f"Invalid status for {kind}: {new_state}", file=sys.stderr)
        return 2
    old_state, error = read_state(path)
    if error:
        print(f"{path}: {error}", file=sys.stderr)
        return 2
    if old_state not in valid:
        print(f"Invalid current status: {old_state}", file=sys.stderr)
        return 2
    if old_state == new_state:
        print(f"Status is already {new_state}.")
        return 0
    allowed = TRANSITIONS[kind][old_state]
    if new_state not in allowed:
        choices = ", ".join(sorted(allowed)) or "none (final status)"
        print(f"Transition not allowed: {old_state} → {new_state}. Allowed: {choices}.", file=sys.stderr)
        return 2
    content = path.read_text(encoding="utf-8")
    updated = STATUS_LINE.sub(f"- **Status:** {new_state}", content, count=1)
    history_change = change or f"Status changed from {old_state} to {new_state}"
    try:
        updated = append_history(updated, history_change, owner)
    except ValueError as error:
        print(f"{path}: {error}", file=sys.stderr)
        return 2
    path.write_text(updated, encoding="utf-8")
    print(f"{path.relative_to(root)}: {old_state} → {new_state}")
    return 0


def command_history(root: Path, relative: str, change: str, owner: str) -> int:
    path = (root / relative).resolve()
    docs_root = documentation_root(root).resolve()
    try:
        path.relative_to(docs_root)
    except ValueError:
        print("The document must be inside the documentation directory.", file=sys.stderr)
        return 2
    if not path.is_file() or path.suffix.lower() != ".md":
        print("History can only be recorded for an existing Markdown document.", file=sys.stderr)
        return 2
    content = path.read_text(encoding="utf-8")
    try:
        updated = append_history(content, change, owner)
    except ValueError as error:
        print(f"{path}: {error}", file=sys.stderr)
        return 2
    path.write_text(updated, encoding="utf-8")
    print(f"History updated: {path.relative_to(root)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="project root (default: current directory)")
    subparsers = parser.add_subparsers(dest="command", required=True)
    list_parser = subparsers.add_parser("list", help="show document status boards")
    list_parser.add_argument(
        "kind", nargs="?", choices=("all", "adr", "spec", "runbook", "guide"),
        help="show all tracked documents or only one document type",
    )
    subparsers.add_parser("check", help="validate documented statuses")
    set_parser = subparsers.add_parser("set-state", help="change status while enforcing transitions")
    set_parser.add_argument("document", help="path relative to the project root, e.g. docs/adr/0001-example.md")
    set_parser.add_argument("status", help="new status")
    set_parser.add_argument("--by", default=getpass.getuser(), help="person or team responsible for the change")
    set_parser.add_argument("--change", help="history entry describing the change")
    history_parser = subparsers.add_parser("history", help="append a dated history entry to a Markdown document")
    history_parser.add_argument("document", help="path relative to the project root")
    history_parser.add_argument("--change", required=True, help="brief description of the document change")
    history_parser.add_argument("--by", default=getpass.getuser(), help="person or team responsible for the change")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "list":
        return command_list(root, None if args.kind in (None, "all") else args.kind)
    if args.command == "check":
        return command_check(root)
    if args.command == "history":
        return command_history(root, args.document, args.change, args.by)
    return command_set(root, args.document, args.status, args.by, args.change)


if __name__ == "__main__":
    raise SystemExit(main())
