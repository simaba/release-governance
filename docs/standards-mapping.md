# Standards and Framework Mapping

This appendix maps the repository's concepts to widely recognized governance themes so teams can align internal operating models with external expectations.

## Purpose

This mapping is not a compliance claim. It is a translation aid that helps teams connect practical release controls to broader governance expectations.

## Conceptual mapping

| Repository concept | External governance theme | Why it maps |
|---|---|---|
| Risk-based release readiness | NIST AI RMF risk management and governance themes | The framework uses explicit risk dimensions and tiered controls rather than uniform release treatment. |
| Intended operating conditions and limitations | Safety case and scope definition concepts | Teams must define where the system is meant to operate and where it is not. |
| Uncertainty handling | AI trustworthiness, robustness, and human awareness themes | Ambiguity and low-confidence behavior must be managed rather than ignored. |
| Fallback and degraded-mode design | Safety engineering and operational resilience themes | Safe failure and graceful degradation are essential in real-world deployment. |
| Monitoring and observability | Post-deployment monitoring and lifecycle oversight themes | AI systems require ongoing operational visibility after release. |
| Human escalation and override | Human oversight and governance themes | Oversight only matters if intervention conditions and authority are clear. |
| Logging and auditability | Accountability, traceability, and assurance themes | Release and incident decisions should be reconstructable and reviewable. |
| Named accountability model | Governance and accountability structure themes | Critical decisions require explicit decision rights and ownership. |

## Examples of useful alignment references

Teams may find it useful to align this framework with:
- NIST AI Risk Management Framework,
- ISO or IEC AI management and assurance standards,
- domain-specific safety and quality management systems,
- internal governance, audit, and change-control processes.

## Practical use

A team can use this mapping in three ways:
1. Translate technical release controls into language that governance stakeholders understand.
2. Show that release readiness is not separate from risk management.
3. Identify missing controls when preparing for internal review or audit.

## Example internal review question set

- Have we defined intended operating conditions and known limitations?
- Is low-confidence behavior handled explicitly?
- Do we have validated degraded-mode behavior?
- Is production monitoring adequate for the identified risk tier?
- Is the accountable approver clearly named?
- Can we reconstruct what happened if an incident occurs?

## Caution

External standards and regulations vary by jurisdiction and domain. Teams should adapt this framework to their own legal, quality, and safety obligations.
