---
name: documentation-workflow
description: Create, review, and maintain project ADRs, Specs, Runbooks, Guides, and documentation indexes using their established status workflows.
---

# Documentation workflow

Use this skill when creating or changing project documentation governed by the software documentation kit.

## Rules

- Read `docs/README.md` and the applicable documents before editing. Treat accepted ADRs as current decisions. Treat Specs in `Approved` or `In Progress` as requirements; a draft or in-review Spec is not approved.
- Follow the document-specific status workflow in `docs/adr/0001-documentation-workflow-and-agent-rules.md` for ADRs, Specs, Runbooks, and Guides. README files and directory indexes do not use workflow statuses. Do not skip, reverse, or claim an approval transition that has not happened.
- Use the matching template and preserve the repository's naming and linking conventions. Keep the document status aligned with its actual review and delivery state.
- For status changes, use `python3 docs/tools/docflow.py set-state <document-path> <new-status>` when available. Run `list` to inspect boards and `check` to validate tracked statuses.
- After each material document-content change, append a `History` row with `python3 docs/tools/docflow.py history <document-path> --change "..." --by "..."`. Include the date through the tool; describe the actual change and identify its responsible owner.
- A `set-state` operation records its own history row automatically. If content also changed, use `--change` with `set-state` to summarize both the edit and transition; do not add a duplicate history row.
- When a change conflicts with an accepted ADR or reveals a lasting decision that is not recorded, explain the conflict and propose a new or superseding ADR before implementing a divergence.
- Update related Specs, ADR links, runbooks, and documentation indexes when the change materially affects them. README files and directory indexes do not use workflow statuses, but material edits to them still receive a history entry.
- If the request asks only for code and no documentation change is warranted, do not create documents solely to satisfy this skill; explain a relevant existing constraint when it affects the implementation.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Added instructions for recording content changes and status transitions in document history. | Project team |
