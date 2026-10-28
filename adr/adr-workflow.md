# ADR workflow

This document describes how to create, review, accept, reject, and replace an Architecture Decision Record (ADR). The authoritative status transitions are defined in [ADR 0001](0001-documentation-workflow-and-agent-rules.md).

## When to create an ADR

Create an ADR for a lasting architectural or technical decision that affects future work, multiple systems, or multiple teams. Keep the decision separate from implementation progress: use a related Spec to track requirements and delivery.

## Workflow

1. **Propose:** Create `NNNN-short-title.md` from the [ADR template](adr-template.md). Set the status to `Proposed`. Record the context, decision being considered, plausible alternatives, consequences, owners, related documents, review conditions, and initial history.
2. **Review:** Ask affected owners to review the context, decision, alternatives, and consequences. Keep the ADR `Proposed` while feedback is unresolved. Update its History when making material edits.
3. **Decide:** Move the ADR to `Accepted` when the decision is approved, or `Rejected` when it is declined. Record the reason and decision in the ADR and History. An accepted ADR is a concluded decision and remains an active constraint; ADRs do not use a `Completed` status.
4. **Apply:** Link the accepted ADR from related Specs or implementation records. Track implementation progress in the related Spec, not by changing the ADR status.
5. **Replace or withdraw:** When an accepted decision changes, create and accept a new ADR that links to the previous one, then move the previous ADR to `Superseded`. Use `Withdrawn` when an accepted decision is no longer applicable and has no replacement. `Rejected`, `Superseded`, and `Withdrawn` are final statuses.

## Status transitions

| Current status | Allowed next status |
|---|---|
| Proposed | Accepted, Rejected |
| Accepted | Superseded, Withdrawn |
| Rejected | None (final) |
| Superseded | None (final) |
| Withdrawn | None (final) |

Do not skip a decision or review step to force a status change. Use the tool to apply valid transitions; it automatically appends a History entry:

```sh
python3 docs/tools/docflow.py list adr
python3 docs/tools/docflow.py set-state docs/adr/0002-short-title.md Accepted --by "Owner" --change "Approved the proposed decision"
```

The path above is for a consuming project with `docs/`. When running from this kit's root, omit the `docs/` prefix.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Added the ADR lifecycle and transition procedure. | Project team |
