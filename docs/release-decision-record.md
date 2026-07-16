# Release Decision Record

A release review should produce an accountable decision, not only a completed checklist. The decision record should show what was reviewed, which evidence was current, what remains uncertain, and who accepted any residual risk or conditions.

## Decision outcomes

Use a small, explicit decision vocabulary.

| Outcome | Meaning |
|---|---|
| **Release** | Required hard gates pass, evidence is sufficient for the stated scope, and no conditions remain. |
| **Release with conditions** | No unresolved blocker remains, but named conditions limit scope, timing, population, authority, monitoring, or follow-up work. |
| **Hold** | Evidence, controls, or remediation are not sufficient for the current release decision. |
| **Do not release** | A critical failure, prohibited condition, or unacceptable residual risk prevents release under the reviewed design. |
| **Defer decision** | The decision owner intentionally postpones judgment until specified evidence or an external dependency becomes available. |

Do not use “approved” without the approved scope, version, environment, and conditions.

## Finding semantics

Keep these concepts separate:

- **Hard gate:** a non-compensable requirement. Failure cannot be offset by a weighted score.
- **Blocker:** an unresolved finding that prevents the current decision.
- **Evidence gap:** missing or unreliable evidence. It may be a blocker depending on the risk and decision.
- **Required action:** follow-up work accepted under a bounded conditional decision.
- **Condition:** a constraint on the released scope or operation.
- **Exception:** authorized deviation from a control, with rationale, owner, expiry, and compensating measures.
- **Residual risk:** risk remaining after controls, explicitly accepted by an authorized owner.
- **Observation:** improvement or concern that does not currently change the decision.

A report should not call the same item both a blocker and an accepted release condition.

## Evidence record

For each material gate or finding, record:

| Field | Purpose |
|---|---|
| Control / question | What release proposition is being tested? |
| System scope | Model, prompt, data, tools, permissions, environment, and population covered |
| Evidence | Report, test, review, run, or artifact used |
| Provenance | Author, system, version, date, and source location |
| Freshness | How long the evidence remains relevant and what changes invalidate it |
| Method | How the result was produced and reviewed |
| Result | pass, fail, partial, not tested, or not applicable with rationale |
| Limitation | Coverage, uncertainty, evaluator, or dependency limits |
| Owner | Person accountable for the control or remediation |
| Disposition | blocker, required action, condition, exception, residual risk, or observation |

Evidence should be traceable to the reviewed system version. A current report about an earlier prompt, model, dataset, permission set, or architecture may not support the current decision.

## Exceptions

An exception record should include:

- control and requirement being deviated from;
- reason the standard path cannot be met;
- affected scope and duration;
- risk introduced;
- compensating controls;
- monitoring and stop conditions;
- accountable approver with authority to accept the risk;
- expiry date;
- remediation or retirement plan;
- evidence required for renewal.

Exceptions should expire. Repeated renewal is evidence that the standard, architecture, or operating model needs review.

## Conditions

A release condition must be enforceable and testable.

Weak condition:

> Monitor closely after launch.

Stronger condition:

> Limit the pilot to 100 authenticated internal users, keep all tools read-only, alert the service owner on any unauthorized tool attempt, and disable the pilot if two critical retrieval-boundary failures occur before the 30-day review.

A condition should state scope, owner, measurement, trigger, and action.

## Residual-risk acceptance

Record:

- risk and affected objective or population;
- evidence supporting the estimate;
- uncertainty and worst credible consequence;
- controls already applied;
- alternatives considered;
- scope and duration of acceptance;
- accepting authority;
- monitoring and stop trigger;
- next review or expiry.

Risk acceptance is a decision, not a checkbox delegated to the author of the report.

## Decision record template

```markdown
# Release decision: [system / version / scope]

**Decision owner:**
**Decision date:**
**Outcome:** release | release with conditions | hold | do not release | defer
**Reviewed scope:** model, prompt, data, tools, permissions, environment, population
**Evidence cutoff:**

## Decision rationale
[Why the evidence supports this outcome.]

## Hard gates
| Gate | Result | Evidence | Limitations | Owner |
|---|---|---|---|---|

## Findings and disposition
| ID | Finding | Severity | Disposition | Owner | Due / expiry |
|---|---|---|---|---|---|

## Conditions and exceptions
| ID | Constraint / deviation | Scope | Monitoring / stop trigger | Approver | Expiry |
|---|---|---|---|---|---|

## Residual risks accepted
| Risk | Evidence and uncertainty | Scope | Accepting owner | Review trigger |
|---|---|---|---|---|

## Changes that invalidate this decision
- model, prompt, retrieval, data, tool, permission, infrastructure, user-population, or policy changes as applicable

## Follow-through
- release or hold action owner:
- evidence-retention location:
- next review:
- incident and rollback owner:
```

## Review questions

Before signing:

- Is the decision owner authorized for the stated scope and residual risk?
- Are hard gates distinct from weighted quality measures?
- Can each material conclusion be traced to current evidence?
- Are missing and not-applicable results explained rather than omitted?
- Are conditions enforceable and monitored?
- Do exceptions expire?
- Are residual risks visible to the accepting owner?
- Are invalidation and regression triggers explicit?
- Can the system be stopped, contained, or rolled back under the reviewed conditions?
