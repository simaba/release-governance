# AI Release Governance Framework

[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-0055A4?style=flat-square)](https://airc.nist.gov/home)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Discussions](https://img.shields.io/badge/Discussions-Join-7289da?style=flat-square&logo=github)](https://github.com/simaba/release-governance/discussions)

A structured framework for governing the full release lifecycle of AI systems, from initial development through production deployment and ongoing monitoring, with specific guidance for regulated industries.

---

## The Problem

Most software release frameworks were not designed for AI systems. AI releases differ from traditional software releases in critical ways:

- **Non-deterministic behavior** — the same model can produce different outputs
- **Data dependency** — model performance degrades as the world changes
- **Emergent risks** — failure modes that were not anticipated during development
- **Regulatory scrutiny** — AI decisions in regulated industries face legal accountability
- **Stakeholder impact** — errors can affect individuals' health, finances, or rights

This framework addresses each of these differences with structured governance gates.

---

## Framework Structure

```text
AI Release Lifecycle
│
├── 1. PRE-DEVELOPMENT
│   ├── Use case approval
│   ├── Risk classification
│   └── Data governance review
│
├── 2. DEVELOPMENT
│   ├── Model card initiation
│   ├── Bias evaluation plan
│   └── Security threat model
│
├── 3. PRE-DEPLOYMENT (Release Gates)
│   ├── Technical validation gate
│   ├── Governance approval gate
│   ├── Legal/compliance gate
│   └── Infrastructure readiness gate
│
├── 4. DEPLOYMENT
│   ├── Staged rollout plan
│   ├── Monitoring activation
│   └── Incident response readiness
│
└── 5. POST-DEPLOYMENT
    ├── Performance monitoring
    ├── Drift detection
    ├── Periodic governance review
    └── Retirement / decommissioning
```

---

## Release Gates

### Gate 1: Technical Validation

| Check | Requirement | Tooling |
|---|---|---|
| Model performance | Meets accuracy/F1 threshold on holdout set | pytest, MLflow |
| Bias evaluation | Disparate impact ratio ≥ 0.80 across subgroups | Fairlearn, AI Fairness 360 |
| Adversarial testing | Red team report completed | Microsoft PyRIT, Giskard |
| Latency / throughput | P99 latency ≤ SLA threshold under load | Locust, k6 |
| Security scan | No critical vulnerabilities in dependencies | Snyk, Dependabot |

### Gate 2: Governance Approval

| Check | Approver | Documentation Required |
|---|---|---|
| AI governance review | AI Governance Lead | Signed governance checklist |
| Risk assessment complete | Risk Officer | Risk register entry |
| Model card complete | Technical Owner | Published model card |
| Explainability report | Technical Owner | SHAP/LIME analysis report |

### Gate 3: Legal & Compliance

| Check | Requirement |
|---|---|
| Regulatory mapping | All applicable regulations identified and addressed |
| Privacy review | GDPR/CCPA impact assessment for personal data |
| Legal sign-off | Legal counsel review for high-risk systems |
| Industry-specific review | HIPAA (healthcare) / SR 11-7 (finance) / state regs |

### Gate 4: Infrastructure Readiness

| Check | Requirement |
|---|---|
| Monitoring configured | Alerts set for performance degradation and drift |
| Logging enabled | All inputs/outputs/decisions logged with retention policy |
| Rollback tested | Rollback to previous version validated in staging |
| Runbook complete | On-call runbook published and reviewed |

---

## NIST AI RMF Alignment

This framework implements the NIST AI RMF **Measure** and **Manage** functions:

- **MS.1** — AI risk identification methods applied at each gate
- **MS.2** — Ongoing monitoring activated at deployment gate
- **MS.3** — Evaluation techniques applied at technical validation gate
- **MG.2** — Risk treatment plans completed before governance gate
- **MG.4** — Rollback and recovery procedures validated at infrastructure gate

Full mapping: [docs/nist-rmf-mapping.md](docs/nist-rmf-mapping.md)

---

## Related Tools

| Tool | Purpose | Link |
|---|---|---|
| Release checklist CLI | Validate release checklist YAML from the command line | [release-checklist](https://github.com/simaba/release-checklist) |
| Regulated AI starter repository | Starting point for governance-ready AI delivery | [regulated-ai](https://github.com/simaba/regulated-ai) |
| Enterprise governance playbook | Full organizational governance playbook | [governance-playbook](https://github.com/simaba/governance-playbook) |

---

## Ecosystem

| Repository | Purpose |
|---|---|
| [governance-playbook](https://github.com/simaba/governance-playbook) | End-to-end governance playbook |
| [release-checklist](https://github.com/simaba/release-checklist) | Release gate framework and CLI |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | NIST AI RMF practitioner guide |
| [ai-prism](https://github.com/simaba/ai-prism) | Curated governance resources |

*Maintained by [Sima Bagheri](https://github.com/simaba) · Connect on [LinkedIn](https://www.linkedin.com/in/simaba/)*
