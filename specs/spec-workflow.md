# Spec workflow

This document describes how to draft, review, approve, implement, complete, or cancel a change Specification (Spec). The authoritative status transitions are defined in [ADR 0001](../adr/0001-documentation-workflow-and-agent-rules.md).

## When to create a Spec

Create a Spec for a change with multiple requirements, meaningful coordination, material risk, or acceptance criteria that need to be reviewed. Create a separate ADR for each lasting architectural decision and link it from the Spec.

## Workflow

1. **Draft:** Create `YYYY-MM-DD-topic.md` from the [Spec template](spec-template.md). Set the status to `Draft`. Describe the problem, goals, scope, requirements, observable acceptance criteria, design, risks, delivery, validation, owners, related documents, and initial history.
2. **Review:** Move the Spec to `In Review` when it is ready for feedback. Reviewers check that requirements and acceptance criteria are clear and that important risks, compatibility, delivery, and validation are addressed. Return it to `Draft` if substantial changes are needed.
3. **Approve:** Move the Spec to `Approved` after the responsible reviewers agree that it is ready to implement. A `Draft` or `In Review` Spec is not an approved requirement.
4. **Implement:** Move the Spec to `In Progress` when implementation begins. Keep requirements, links, and History current as the work reveals material changes. Record new lasting decisions in ADRs.
5. **Complete:** Move the Spec to `Completed` only after its acceptance criteria have been checked and the planned delivery is done. `Completed` is final.
6. **Cancel:** Move a Spec to `Cancelled` when the change will not proceed. Cancellation is allowed from `Draft`, `In Review`, `Approved`, or `In Progress`; explain why in the document and History. `Cancelled` is final.

## Status transitions

| Current status | Allowed next status |
|---|---|
| Draft | In Review, Cancelled |
| In Review | Draft, Approved, Cancelled |
| Approved | In Progress, Cancelled |
| In Progress | Completed, Cancelled |
| Completed | None (final) |
| Cancelled | None (final) |

Use the CLI to inspect and change states. It rejects transitions outside this workflow and automatically appends a History entry:

```sh
python3 docs/tools/docflow.py list spec
python3 docs/tools/docflow.py set-state docs/specs/2026-10-28-topic.md "In Review" --by "Owner" --change "Submitted the Spec for review"
```

For material content edits that do not change status, append a History entry directly through the tool:

```sh
python3 docs/tools/docflow.py history docs/specs/2026-10-28-topic.md --change "Clarified acceptance criteria" --by "Owner"
```

The paths above are for a consuming project with `docs/`. When running from this kit's root, omit the `docs/` prefix.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Added the Spec lifecycle and transition procedure. | Project team |
