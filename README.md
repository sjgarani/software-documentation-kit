# Project documentation

This repository contains documentation templates and lightweight tools for keeping project decisions, specifications, and operational procedures alongside code. To use the kit in another repository, run `bash tools/install.sh /path/to/project`. The installer copies the kit into the target project's `docs/` directory and adds its agent instructions to the root `AGENTS.md`.

## Contents

- `adr/`: architectural and technical decisions with lasting effects.
- `specs/`: requirements and proposals for significant changes.
- `tools/docflow.py`: dependency-free CLI for tracking document statuses.
- `tools/skills/documentation-workflow/`: reusable agent skill for maintaining documentation and statuses.

## Getting started

1. For a change with substantial requirements or coordination, copy [the Spec template](specs/spec-template.md) to `YYYY-MM-DD-topic.md`.
2. For a lasting technical decision, use [the ADR template](adr/adr-template.md) and name the file `NNNN-short-title.md`.
3. Install the kit in another repository with `bash tools/install.sh /path/to/project`.

## Conventions

- Write documentation in English and use relative links within `docs/`.
- Name ADRs with a sequential number and short title: `NNNN-short-title.md`.
- Name Specs with a date and topic: `YYYY-MM-DD-topic.md`.
- Include status, owner, and related links in status-tracked documents. README files and directory indexes are reviewed without a workflow status.
- Mark superseded documents and link to their replacements; preserve decision history.
- Keep documentation with the related code and review it alongside relevant changes.

The [ADR 0001](adr/0001-documentation-workflow-and-agent-rules.md) defines the document states, workflow, history, and agent rules. The installer places the `documentation-workflow` skill in `.agents/skills/`. After installation, use `python3 docs/tools/docflow.py list`, `check`, `set-state`, or `history` from the target project.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Documented the history process and CLI commands. | Project team |
| 2026-10-28 | Removed Guides and Runbooks from the main-branch documentation scope. | Project team |
