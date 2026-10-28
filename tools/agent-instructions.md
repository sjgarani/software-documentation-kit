## Documentation rules for agents

- Before planning or changing code, read `docs/README.md` and the ADRs and Specs relevant to the task.
- Follow ADRs with status `Accepted`. They are the current rules for the decisions they cover; do not silently contradict them.
- Specs with status `Approved` or `In Progress` define requirements and acceptance criteria. Specs with status `Draft` or `In Review` are not approved; do not treat proposals as final decisions.
- If a task conflicts with an accepted ADR or requires an unrecorded lasting decision, explain the conflict and propose updating or creating an ADR before implementing a divergence.
- When working on a change tracked by a Spec, keep its status and History section current. Do not mark a Spec `Completed` until its acceptance criteria have been checked.
- Use `python3 docs/tools/docflow.py list` and `python3 docs/tools/docflow.py check` to inspect and validate statuses. Status changes must follow the transitions in ADR 0001.
- Keep the final `History` section current after material edits. The tool records status transitions automatically and provides `python3 docs/tools/docflow.py history` for other documentation changes.
- Use the `documentation-workflow` skill in `.agents/skills/documentation-workflow/SKILL.md` when creating, reviewing, or updating ADRs, Specs, or the project README.

## History

| Date | Change | Owner |
|---|---|---|
| 2026-10-28 | Added the requirement to maintain document history. | Project team |
| 2026-10-28 | Limited documentation workflow instructions on main to ADRs and Specs. | Project team |
