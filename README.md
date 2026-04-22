# AI Release Governance Framework

[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-0055A4?style=flat-square)](https://airc.nist.gov/home)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Discussions](https://img.shields.io/badge/Discussions-Join-7289da?style=flat-square&logo=github)](https://github.com/simaba/release-governance/discussions)

A structured framework for governing the release lifecycle of AI systems, from development through deployment, monitoring, and retirement.

## Choose this repo when

Use this repository when you need the **release-stage lifecycle framework** for AI systems:

- release gates
- stage-specific approval criteria
- deployment readiness structure
- post-release governance expectations

Do **not** start here if you need a working config validator. Use [`release-checklist`](https://github.com/simaba/release-checklist) for that.

Do **not** start here if you need the broader organizational operating model. Use [`governance-playbook`](https://github.com/simaba/governance-playbook).

## Framework structure

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
├── 3. PRE-DEPLOYMENT
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

## Release gates

### Gate 1: Technical validation

| Check | Requirement | Tooling |
|---|---|---|
| Model performance | Meets accuracy/F1 threshold on holdout set | pytest, MLflow |
| Bias evaluation | Disparate impact ratio ≥ 0.80 across subgroups | Fairlearn, AI Fairness 360 |
| Adversarial testing | Red-team report completed | Microsoft PyRIT, Giskard |
| Latency / throughput | P99 latency ≤ SLA threshold under load | Locust, k6 |
| Security scan | No critical vulnerabilities in dependencies | Snyk, Dependabot |

### Gate 2: Governance approval

| Check | Approver | Documentation required |
|---|---|---|
| AI governance review | AI Governance Lead | Signed governance checklist |
| Risk assessment complete | Risk Officer | Risk register entry |
| Model card complete | Technical Owner | Published model card |
| Explainability report | Technical Owner | SHAP/LIME analysis report |

### Gate 3: Legal and compliance

| Check | Requirement |
|---|---|
| Regulatory mapping | Applicable regulations identified and addressed |
| Privacy review | Privacy impact assessment completed where required |
| Legal sign-off | Legal counsel review for high-risk systems |
| Industry-specific review | Domain-specific obligations addressed |

### Gate 4: Infrastructure readiness

| Check | Requirement |
|---|---|
| Monitoring configured | Alerts set for degradation and drift |
| Logging enabled | Inputs, outputs, and decisions logged with retention policy |
| Rollback tested | Rollback to previous version validated in staging |
| Runbook complete | On-call runbook published and reviewed |

## NIST AI RMF alignment

This framework primarily operationalizes the **Measure** and **Manage** functions.

Full mapping: [docs/nist-rmf-mapping.md](docs/nist-rmf-mapping.md)

## Related repositories

| Repository | What it adds |
|---|---|
| [release-checklist](https://github.com/simaba/release-checklist) | Working CLI validator for YAML-based release configs |
| [governance-playbook](https://github.com/simaba/governance-playbook) | Broader organizational operating model |
| [regulated-ai](https://github.com/simaba/regulated-ai) | Starter repo with governance and release artifacts |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | Practitioner implementation guide |

*Maintained by [Sima Bagheri](https://github.com/simaba)*
