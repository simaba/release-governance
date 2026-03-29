# Accountability RACI for AI Release Governance

This document converts the accountability principles into an operational decision-rights model.

## Roles

Example roles:
- Product lead
- Engineering lead
- ML lead
- Operations or SRE lead
- Quality or safety representative
- Compliance or legal representative
- Release approver

Teams can rename or merge roles based on their operating model.

## Example RACI

| Activity | Product | Engineering | ML | Ops or SRE | Quality or Safety | Compliance or Legal | Release approver |
|---|---|---|---|---|---|---|---|
| Define intended operating conditions | A | R | C | I | C | C | I |
| Document known limitations | A | R | R | I | C | C | I |
| Specify uncertainty handling | C | A | R | C | C | I | I |
| Design degraded mode and fallback | C | A | R | C | C | I | I |
| Validate monitoring coverage | I | R | C | A | C | I | I |
| Define alert thresholds | I | R | C | A | C | I | I |
| Define human override and escalation | A | R | C | R | C | C | I |
| Prepare incident response playbook | I | R | C | A | C | C | I |
| Recommend release decision | A | R | C | C | C | C | I |
| Approve release | C | C | I | C | C | C | A |
| Own post-release incident response | I | R | C | A | C | C | I |
| Own post-release improvement actions | A | R | R | C | C | I | I |

Legend:
- R = Responsible
- A = Accountable
- C = Consulted
- I = Informed

## Design rules

A practical accountability model should satisfy the following:
- every critical release activity has exactly one accountable owner,
- monitoring and incident response are not left implicit,
- release approval is separate from evidence generation where appropriate,
- human override is paired with actual authority and operational context.

## Common failure modes

Watch for these patterns:
- everyone is responsible, so no one is accountable,
- operations own production issues but were not part of release design,
- compliance is consulted too late,
- override responsibility exists on paper but without authority or tooling.

## Minimum accountability checks for high-risk releases

Before launch, verify that:
- the accountable release approver is named,
- the owner of monitoring and alert response is named,
- the owner of disablement or rollback is named,
- the owner of post-release follow-up actions is named.
