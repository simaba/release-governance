# Post-Release Monitoring Plan

Use this template to define what will be watched after launch and who will respond.

## Release details
- Feature name:
- Release identifier:
- Launch date:
- Risk tier:
- Monitoring owner:

## Core monitoring questions
- What abnormal behavior would indicate rising risk?
- What patterns would suggest drift, misuse, or unsupported usage?
- What signals should trigger fallback, disablement, or review?

## Signals and thresholds
| Signal | Why it matters | Threshold | Owner | Action if exceeded |
|---|---|---|---|---|
| Low-confidence rate | Indicates uncertainty or domain mismatch |  |  |  |
| Fallback invocation rate | Indicates degraded behavior frequency |  |  |  |
| Incident or complaint count | Indicates user-facing quality or safety concerns |  |  |  |
| Abnormal response category rate | Indicates harmful or unexpected outputs |  |  |  |
| Override or disablement events | Indicates operational instability |  |  |  |

## Review cadence
- Daily review during initial launch window:
- Weekly review after stabilization:
- Formal review date:

## Response plan
- Who reviews alerts first:
- Who can trigger rollback or disablement:
- Who approves wider rollout:
- Who owns corrective actions:

## Notes
Document the rationale for each threshold and update this plan as the operating context evolves.
