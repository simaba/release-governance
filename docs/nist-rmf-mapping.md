# NIST AI RMF Practitioner Cross-Reference

This document explains how the release-governance artifacts can support internal work related to the NIST AI Risk Management Framework (AI RMF 1.0).

It is not an official NIST mapping, assessment, profile, conformity determination, or claim that the repository implements every category or subcategory. Exact applicability depends on the organization, system context, evidence, and how the artifacts are actually used.

Use the official NIST material as the authoritative source. Treat this page as a navigation aid for practitioner discussions.

## Cross-reference by function

### GOVERN

Release-governance artifacts can support governance work by recording:

- release and residual-risk decision authority;
- control, evidence, incident, exception, and rollback owners;
- review outcomes and conditions;
- change and invalidation triggers;
- exception expiry and renewal;
- evidence retention and accountability expectations.

Relevant repository artifact:

- [`release-decision-record.md`](release-decision-record.md)

What this repository does not establish on its own:

- enterprise policy approval;
- board or executive oversight;
- workforce competence;
- supplier governance;
- legal or regulatory applicability;
- organization-wide risk culture.

### MAP

Release preparation can support contextualization by documenting:

- intended use and prohibited uses;
- users and affected populations;
- deployment environment and geography;
- model, prompt, retrieval, data, tool, permission, and action scope;
- foreseeable misuse and failure consequences;
- reversibility and operational dependencies;
- rollout population and exposure limit.

What this repository does not establish on its own:

- complete stakeholder impact assessment;
- authoritative categorization of all risks;
- scientific validity of the system;
- complete legal or societal context;
- representation of every affected group.

### MEASURE

Release evidence can support measurement work by documenting:

- evaluation scope and operating-population assumptions;
- hard-gate and quality-measure definitions;
- evaluator method and limitations;
- security, privacy, safety, and operational control tests;
- slice and failure analysis;
- uncertainty, exclusions, and evidence freshness;
- monitoring and regression evidence.

Companion repository:

- [`agent-eval`](https://github.com/simaba/agent-eval)

What this repository does not establish on its own:

- benchmark validity;
- calibrated thresholds;
- evaluator reliability;
- complete safety or security testing;
- sufficient statistical power;
- production representativeness.

### MANAGE

Release decisions and follow-through can support risk treatment by recording:

- release, conditional release, hold, rejection, or deferral;
- blockers, required actions, conditions, exceptions, and observations;
- residual-risk acceptance;
- staged exposure and expansion criteria;
- monitoring and stop triggers;
- rollback, containment, recovery, and incident ownership;
- expiry and re-evaluation conditions.

What this repository does not establish on its own:

- that selected treatments are effective;
- that residual risk is legally or ethically acceptable;
- that operational teams can execute the response;
- that downstream impacts are fully remediated;
- that the decision authority is appropriate for every jurisdiction or harm.

## Artifact-to-question view

| Release-governance question | AI RMF function most directly supported | Evidence still needed outside the template |
|---|---|---|
| Who owns the release and residual-risk decision? | Govern | actual organizational authority and policy |
| What system, users, actions, and environment are in scope? | Map | validated context and affected-stakeholder input |
| Which hard gates and measures support the decision? | Measure | valid test design, data, evaluator, and results |
| What failures, uncertainty, and evidence gaps remain? | Measure / Manage | investigation and domain judgment |
| Which conditions, exceptions, or residual risks are accepted? | Govern / Manage | authorized decision and enforceable controls |
| How can exposure be stopped, contained, or rolled back? | Manage | tested operational capability |
| Which changes invalidate the decision? | Govern / Manage | working change-detection and regression process |

## How to use this cross-reference

1. Start with the official AI RMF function, category, and subcategory relevant to your organization.
2. Identify which internal decision or evidence need it creates.
3. Use repository artifacts only where they help record that work.
4. Link to authoritative policies, tests, assessments, and owners outside the repository.
5. Record gaps instead of marking a category implemented because a template exists.
6. Review the mapping when NIST guidance, the system, or the organizational process changes.

## Common misuse

Avoid statements such as:

- “The repository is NIST compliant.”
- “Completing the template implements the AI RMF.”
- “A release decision record proves the control is effective.”
- “A cross-reference is an audit result.”

A template can improve structure and traceability. The quality of the evidence, decisions, controls, and outcomes determines whether the work is meaningful.

---

*Practitioner cross-reference maintained by [Sima Bagheri](https://github.com/simaba). Not affiliated with or endorsed by NIST.*
