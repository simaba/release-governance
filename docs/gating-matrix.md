# Operational Gating Matrix

This document translates the framework into a concrete, risk-tiered release model that a team can use during go or no-go review.

## Gate definitions

| Gate | What must be true |
|---|---|
| G1. Domain and data coverage | Intended operating conditions, known limitations, and out-of-scope scenarios are documented. |
| G2. Uncertainty handling | Confidence thresholds, uncertainty indicators, and behavior under ambiguous inputs are defined. |
| G3. Fallback and degraded mode | Safe fallback or degraded operation is implemented, validated, and explicitly triggered by known conditions. |
| G4. Monitoring and observability | Production signals, dashboards, alert thresholds, and ownership for monitoring are defined. |
| G5. Human escalation and override | Human intervention conditions, authority, and escalation routes are documented and operational. |
| G6. Incident response and recovery | Disablement, rollback, containment, and response playbooks are prepared and tested. |
| G7. Accountability sign-off | Named accountable owners and approvers are identified for release and post-release response. |
| G8. Post-release review plan | Review window, success metrics, drift indicators, and follow-up actions are planned. |

## Required controls by risk tier

| Risk tier | Minimum required gates | Required evidence | Required reviewers | Release constraints |
|---|---|---|---|---|
| Low | G1, G2, G4 | Scope and limitations note, basic monitoring plan | Product, engineering | Limited rollout preferred, rollback available |
| Medium | G1, G2, G3, G4, G5, G8 | Test evidence for degraded behavior, escalation path, monitoring thresholds | Product, engineering, operations, quality or compliance as applicable | Phased rollout, enhanced review frequency, launch criteria explicitly documented |
| High | G1, G2, G3, G4, G5, G6, G7, G8 | Formal evidence package, validated rollback or disablement, explicit accountability map, incident playbook drill or equivalent proof | Product, engineering, operations, quality, safety, security, compliance or legal as applicable | Strict rollout control, explicit go or no-go meeting, rapid disablement path, mandatory post-release review |

## Suggested go or no-go logic

### Low risk
- Go if all required gates are satisfied and there is a rollback path.
- Conditional go only if the open items are minor and do not affect control, monitoring, or scope clarity.

### Medium risk
- Go only if all required gates are satisfied.
- Conditional go only with named owner, deadline, and compensating control.
- No-go if degraded-mode, monitoring, or escalation design is incomplete.

### High risk
- Go only if all required gates are satisfied and accountable approvers explicitly sign off.
- No-go if any of the following are missing:
  - safe degraded behavior,
  - production monitoring ownership,
  - incident disablement or rollback mechanism,
  - named accountable owner for post-release incidents.

## Evidence package checklist

A practical evidence package can include:
- system scope and intended operating conditions,
- known limitations and out-of-scope scenarios,
- uncertainty handling specification,
- degraded-mode test results,
- monitoring dashboard definition,
- alert thresholds and on-call owner,
- escalation and override rules,
- incident response playbook,
- release approver list,
- post-release review date and metrics.

## Notes

This matrix is intentionally lightweight. Teams should adapt the reviewer set and evidence depth to the product, jurisdiction, and regulatory context.
