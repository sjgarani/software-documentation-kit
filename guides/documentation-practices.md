# Software documentation practices

- **Status:** Published

## Choose a document by the question

- **ADR:** “What decision did we make, why, and what effects do we expect?” Use it for choices that are hard to reverse or affect multiple people, systems, or future changes. An ADR records one decision, not an entire specification.
- **Spec:** “What needs to change, and how will we know it is correct?” Use it for changes with multiple requirements, cross-functional work, risks, or design alternatives. One Spec may link to several ADRs.
- **Runbook:** “How do we operate, diagnose, or recover the service?” Write it for someone under pressure, with verifiable steps and useful links.
- **Guide:** “How do we perform this recurring activity?” Use it for stable knowledge that does not belong to one delivery.
- **README:** “What is this project, and how do I get started?” Keep it short and point to details.

## ADRs that remain useful

- Write the context before the decision. Constraints and forces make the choice understandable later.
- Record plausible alternatives and why they were chosen or rejected. Avoid artificial lists of options that were never considered.
- Prefer atomic decisions. If two decisions are independent, create separate ADRs and link them.
- Give each ADR an explicit status. When a decision changes, create a new ADR that supersedes the previous one and link both documents.
- Record positive and negative consequences, including operational cost and accepted debt.
- Do not rewrite history to make a decision seem inevitable. Keep the record faithful to what was known at the time.

## Actionable Specs

- Start with the problem and affected people or systems, not the preferred solution.
- Separate goals from out-of-scope items to prevent silent expansion.
- Write observable acceptance criteria. Prefer “given/when/then” over vague terms such as “fast” or “secure.”
- Separate required behavior from implementation details that may still change.
- State uncertainties explicitly and identify an owner or resolution condition.
- Include deployment, compatibility, migration, observability, and rollback where relevant.
- Keep the Spec current during implementation. Record material changes and decisions in ADRs.

## Maintenance and workflow

- Keep documents in the same repository as related code where possible; this makes joint review and history easier.
- Review documentation in pull requests alongside code, with effort proportional to risk.
- Do not document every line of code. Clear names, types, tests, and local comments explain implementation details better. Document intent, contracts, limits, and non-obvious reasons.
- Avoid duplicating information. Choose one source of truth and link to it.
- Use direct language, consistent terms, small examples, and ISO dates (`YYYY-MM-DD`).
- Set review conditions for operational or change-prone documents. Archive or mark obsolete content as superseded, and correct dangerous instructions as soon as they are found.
- Do not include passwords, tokens, personal data, or restricted information in versioned documents.
- Follow the state transitions in [ADR 0001](../adr/0001-documentation-workflow-and-agent-rules.md). Use `python3 docs/tools/docflow.py list` to track documents and `check` to validate statuses.
- Keep a `History` table at the end of maintained documents. Use `python3 docs/tools/docflow.py history <document> --change "..." --by "..."` after material content changes; status transitions are logged automatically by `set-state`.
- Treat accepted ADRs as constraints for future changes. If a change requires a different decision, propose a new ADR linked to the previous one before implementing the divergence.

## Suggested lightweight workflow

1. Small, local change: use an issue or pull request with context and validation; skip a separate document if it adds no value.
2. Change with substantial requirements or coordination: draft a Spec, review it, implement it, and update it to reflect the result.
3. Significant architectural choice during a Spec: create a separate ADR and link it from the Spec.
4. Change affecting operations: update or create a runbook, alerts, and rollback instructions.
5. After delivery: mark the Spec completed and link to implementation and decisions.

Teams can simplify or extend this workflow based on risk, regulation, and scale. The goal is to reduce lost context and rework, not to maximize document count.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Published documentation practices and status workflows. | Project team |
| 2026-10-28 | Added the required History table process and CLI usage. | Project team |
