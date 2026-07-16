# AI Release Governance Framework

[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Informed-0055A4?style=flat-square)](https://airc.nist.gov/home)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

A practitioner framework for turning evaluation, control, operational, and risk evidence into an accountable AI release decision.

The repository is deliberately broader than a checklist and narrower than an enterprise governance operating model. It focuses on the release boundary: what proposition is being approved, which evidence supports it, what remains uncertain, and who owns the decision, conditions, exceptions, residual risks, and rollback.

## Start here

| Artifact | Use it for |
|---|---|
| [`docs/release-decision-record.md`](docs/release-decision-record.md) | decision outcomes, evidence fields, finding dispositions, conditions, exceptions, and residual-risk acceptance |
| [`docs/nist-rmf-mapping.md`](docs/nist-rmf-mapping.md) | cautious practitioner cross-reference to NIST AI RMF functions |
| [`release-checklist`](https://github.com/simaba/release-checklist) | executable YAML validation for a narrower set of release-readiness fields |
| [`governance-playbook`](https://github.com/simaba/governance-playbook) | broader organizational operating model and recurring governance forums |

## A release decision is scoped

“Release” should always identify:

- system and version;
- model, prompt, retrieval, data, tools, and permissions in scope;
- environment and infrastructure configuration;
- user population and geography;
- enabled actions and external effects;
- rollout stage and exposure limit;
- evidence cutoff date;
- decision owner and authority;
- conditions, exceptions, and expiry;
- changes that invalidate the decision.

Approval of one configuration should not be interpreted as approval of future model, prompt, data, tool, permission, or population changes.

## Lifecycle

```text
purpose and risk context
        ↓
release proposition and scope
        ↓
evidence plan and hard gates
        ↓
evaluation and control verification
        ↓
operational / containment readiness
        ↓
release decision and dispositions
        ↓
staged rollout and verification
        ↓
monitoring, incident, change, and retirement
```

Release governance begins before the final review. The evidence plan, owners, hard gates, and invalidation triggers should be agreed before teams optimize against a convenient metric set.

## Gate design

A gate should ask a decision-relevant question, identify the evidence needed, and define the possible dispositions.

### 1. Purpose, scope, and risk context

Evidence should establish:

- intended use, users, and prohibited uses;
- affected people and foreseeable misuse;
- authority, data, and tool boundaries;
- reversibility and worst credible consequences;
- applicable internal and external obligations;
- owner and release authority.

### 2. Evaluation validity

Evidence should establish:

- task and risk coverage;
- operating-population assumptions and exclusions;
- hard-gate and quality-measure definitions;
- evaluator validity and adjudication;
- repeated-run policy and uncertainty;
- slice results and material failures;
- regression coverage.

Do not rely on an aggregate score without reviewing critical failures and non-compensable conditions.

### 3. Security, privacy, safety, and policy controls

Evidence should establish that relevant controls are:

- defined against the actual system scope;
- enforced in the deployment path;
- tested under normal, adversarial, and failure conditions;
- attributable to a current version;
- supported by exception and incident processes;
- subject to named ownership and change control.

Avoid prescribing a particular tool or explanation technique as universally required. The evidence method should fit the system, decision, and risk.

### 4. Operational and containment readiness

Evidence should cover:

- service objectives and capacity assumptions;
- observability at the agent, tool, workflow, and outcome levels;
- rollback, disable, and credential-revocation paths;
- partial and uncertain external actions;
- data and state recovery;
- on-call and incident decision rights;
- user support and redress where applicable;
- evidence retention with privacy controls.

A rollback test should verify the resulting state, not only demonstrate that an earlier software version can be redeployed.

### 5. Decision and follow-through

The review should distinguish:

| Term | Meaning |
|---|---|
| Hard gate | non-compensable requirement |
| Blocker | unresolved condition preventing the current decision |
| Evidence gap | missing or unreliable support for a proposition |
| Required action | follow-up work accepted under a bounded conditional release |
| Condition | enforceable limit on scope or operation |
| Exception | authorized deviation with compensating controls and expiry |
| Residual risk | remaining risk accepted by an authorized owner |
| Observation | improvement that does not currently change the decision |

See [`docs/release-decision-record.md`](docs/release-decision-record.md) for a template and review questions.

## Decision outcomes

| Outcome | Use when |
|---|---|
| **Release** | required hard gates pass and no conditions remain |
| **Release with conditions** | no blocker remains, but enforceable constraints or required actions limit the release |
| **Hold** | evidence, remediation, or control readiness is insufficient |
| **Do not release** | critical failure, prohibited condition, or unacceptable residual risk remains |
| **Defer decision** | the owner postpones judgment until specified evidence or dependency is available |

A conditional release must not relabel an unresolved blocker as a future action. Conditions should state scope, owner, measurement, stop trigger, and expiry.

## Evidence quality

For each material conclusion, record:

- proposition or control being assessed;
- system scope and version;
- evidence source, author, date, and location;
- method and reviewer;
- result and uncertainty;
- coverage and exclusions;
- freshness and invalidation trigger;
- owner and disposition.

A current document can contain stale evidence. Freshness depends on whether the reviewed system and operating conditions have changed, not only the file date.

## Staged release

A staged rollout is a control only when it has:

- a defined population and exposure limit;
- monitoring linked to plausible failures;
- named go/no-go decision points;
- stop and rollback authority;
- minimum evidence for expansion;
- user support and incident response;
- conditions that prevent silent scope growth.

“Pilot” should not become an indefinite production state without renewed evidence and an accountable decision.

## Change control

Re-evaluate when material changes occur to:

- model or provider;
- prompt, policy, routing, or orchestration;
- retrieval corpus or data distribution;
- tools, permissions, identities, or action authority;
- infrastructure or deployment region;
- user population or use case;
- evaluator, rubric, threshold, or test set;
- relevant law, policy, or internal control;
- known failure or incident evidence.

The prior decision record should state which changes invalidate it.

## Maturity and scope

This is a practitioner framework for planning and reviewing AI releases. It is not a certified release process, safety case, regulatory approval, legal determination, or substitute for qualified security, privacy, safety, compliance, operational, and domain review.

References to NIST AI RMF and other governance concepts are practitioner mappings. Verify official sources and adapt the framework to the actual authority, population, risk, and jurisdiction.

## Related repositories

| Repository | Distinct role |
|---|---|
| [`release-checklist`](https://github.com/simaba/release-checklist) | working config validator |
| [`agent-eval`](https://github.com/simaba/agent-eval) | evaluation validity and decision semantics |
| [`accountability-patterns`](https://github.com/simaba/accountability-patterns) | decision rights, human review, provenance, and redress |
| [`regulated-ai`](https://github.com/simaba/regulated-ai) | starter repository structure and templates |

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
