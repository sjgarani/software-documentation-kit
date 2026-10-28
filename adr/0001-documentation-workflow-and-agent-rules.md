# ADR-0001: Documentation workflow and agent rules

- **Status:** Accepted
- **Date:** 2026-10-28
- **Owners:** project team
- **Related:** [documentation practices](../guides/documentation-practices.md), [Spec template](../specs/spec-template.md)

## Context

Projects adopting this kit need to track architectural decisions and specified changes. The templates include statuses, but do not define transition rules, a simple way to inspect documents, or instructions for coding agents to treat accepted decisions as implementation constraints.

## Decision

Use the document statuses defined by this kit as the source of truth and keep them in the Markdown files. Track the progress of a change in its related Spec; ADRs track the lifecycle of a decision, not implementation task progress.

The valid statuses and transitions are:

- **ADR:** `Proposed` → `Accepted` or `Rejected`; `Accepted` → `Superseded` or `Withdrawn`. Final statuses have no outgoing transitions. A changed decision requires a new ADR linked to the previous one.
- **Spec:** `Draft` → `In Review` or `Cancelled`; `In Review` → `Draft`, `Approved`, or `Cancelled`; `Approved` → `In Progress` or `Cancelled`; `In Progress` → `Completed` or `Cancelled`. Final statuses have no outgoing transitions.
- **Runbook:** `Draft` → `In Review`; `In Review` → `Draft`, `Active`, or `Retired`; `Active` → `In Review` or `Retired`. `Retired` is final. Move an Active runbook to In Review when its procedure needs verification or revision.
- **Guide:** `Draft` → `In Review`; `In Review` → `Draft`, `Published`, or `Retired`; `Published` → `In Review` or `Retired`. `Retired` is final. Use In Review when a published guide needs substantive updates.

README files and directory index pages are not status-tracked; keep them current through ordinary documentation review. The kit provides `tools/docflow.py`, a Python tool with no external dependencies. It lists ADRs, Specs, Runbooks, and Guides; validates their statuses; and allows only permitted transitions when changing a status. It does not replace review, Git history, approval, or task management.

Every maintained document ends with a `History` table using the columns `Date`, `Change`, and `Owner`. Templates include this section. The `history` command appends entries for material content changes. `set-state` records each status transition automatically; its optional `--change` argument can include the reason or summarize related edits. Agents using the installed skill must record material documentation edits and must not create a separate history entry for a transition already recorded by `set-state`.

When the kit is installed, its instructions are added to the project root `AGENTS.md` in a marked block, preserving existing content and avoiding duplication. The `documentation-workflow` skill is installed under `.agents/skills/` to guide agents through document selection, status transitions, and updates. Before proposing or implementing changes, agents must consult applicable documents and follow accepted ADRs and approved or in-progress Specs. They must record conflicts or the need for a documentation change before diverging from a decision. Draft and in-review Specs are not approved requirements.

## Alternatives considered

### Keep statuses without a tool, skill, or agent rules

- Advantages: no additional tools or configuration.
- Disadvantages: makes it harder to track multiple documents and leaves enforcement of decisions to informal instructions.
- Reason for rejection: does not meet the need for consistent tracking in adopting projects.

### Use an external workflow management platform

- Advantages: may provide broader dashboards, permissions, and automation.
- Disadvantages: adds a dependency and may duplicate the status kept in version-controlled documents.
- Reason for rejection: the kit should work in common repositories without an additional service.

## Consequences

### Benefits

- Status is kept with each document and tracked in Git revisions.
- The CLI provides a quick overview and detects invalid statuses or disallowed transitions.
- Adopting projects get explicit agent instructions without losing their existing `AGENTS.md` content.

### Costs and risks

- The tool validates syntax and transitions, but cannot determine whether a decision is sound or a Spec has actually been implemented.
- Installation copies the kit files; future updates must be applied deliberately to preserve local customizations.
- The workflow is intentionally simple and may need to evolve if a concrete need for approvals or additional statuses arises.

### Follow-up actions

- [x] Document statuses, transitions, and history requirements for each tracked document type.
- [x] Provide the tracking CLI.
- [x] Provide a history command, installer, agent instructions, and a reusable workflow skill.

## Review

Revisit this decision if additional statuses are needed, approvals must be tracked beyond Git, or recurring conflicts arise between Specs and ADRs.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Defined the History section and automated history recording for document updates and status transitions. | Project team |
