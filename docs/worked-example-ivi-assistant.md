# Worked Example: IVI Voice Assistant Release Review

This example shows how the framework can be applied to a hypothetical in-vehicle voice assistant feature that uses AI for intent handling and response generation.

## Scenario

Feature: AI-enabled in-vehicle voice assistant for infotainment and navigation support.

Example behaviors:
- answers user questions about vehicle functions,
- interprets navigation-related intents,
- escalates to deterministic fallback for unsupported or low-confidence requests.

Deployment context:
- regulated market,
- safety-adjacent environment,
- user-facing feature with brand and compliance risk.

## Step 1: Define the risk inputs

Illustrative input values on a 1 to 5 scale:

- Safety impact: 4
- Regulatory exposure: 4
- Uncertainty sensitivity: 4
- Operational complexity: 4
- Observability maturity: 3
- Fallback readiness: 4

## Step 2: Compute the risk score

Using the scaffold in `src/risk_scoring.py`:

- Base risk drivers = 4 + 4 + 4 + 4 = 16
- Risk reducers = (3 - 1) + (4 - 1) = 5
- Final score = 11
- Resulting tier = Medium

Interpretation:
The system is not classified as high risk in this example because fallback readiness is reasonably mature and monitoring is partially established. However, it still requires stronger controls than an ordinary low-risk feature release.

## Step 3: Apply the gating matrix

For a medium-risk release, the minimum required gates are:
- G1. Domain and data coverage
- G2. Uncertainty handling
- G3. Fallback and degraded mode
- G4. Monitoring and observability
- G5. Human escalation and override
- G8. Post-release review plan

## Step 4: Assess release evidence

### Example evidence status

| Area | Status | Notes |
|---|---|---|
| Intended operating conditions defined | Yes | Supported domains and non-supported request types documented |
| Known limitations documented | Yes | Unsupported requests and out-of-scope scenarios listed |
| Uncertainty handling specified | Yes | Low-confidence threshold defined with fallback routing |
| Safe degraded mode validated | Yes | Deterministic fallback path tested for unsupported intents |
| Production monitoring defined | Partial | Core telemetry available, but alert thresholds still being tuned |
| Human escalation path defined | Yes | Customer-facing escalation path and internal owner named |
| Post-release review scheduled | Yes | 30-day review planned with quality, product, and operations |

## Step 5: Make the release decision

### Decision
Conditional go.

### Reasoning
- The medium-risk release gates are largely satisfied.
- The remaining gap is not the existence of monitoring, but the maturity of production thresholds.
- A conditional go can be justified if the missing thresholds are owned, dated, and covered by a compensating control during limited rollout.

### Conditions attached to launch
- Limited rollout only.
- Named owner for monitoring threshold completion before wider expansion.
- Daily review of key incident indicators during the initial launch window.
- Immediate fallback to deterministic mode if abnormal behavior exceeds pre-defined tolerance.

## Step 6: Accountability map

| Decision area | Accountable | Responsible contributors |
|---|---|---|
| Release recommendation | Product lead | Engineering, quality, operations |
| Technical readiness evidence | Engineering lead | ML, software, systems teams |
| Monitoring readiness | Operations lead | Engineering, observability owner |
| Risk acceptance | Designated release approver | Product, quality, compliance |
| Incident disablement | Operations lead | Engineering on-call |

## Step 7: Post-release review plan

Review at 7, 14, and 30 days:
- low-confidence rate,
- fallback invocation rate,
- abnormal response categories,
- customer complaints or incident tickets,
- disablement or rollback events,
- drift or expansion of unsupported usage patterns.

## Key lesson

The framework does not force a binary answer too early. It turns vague concerns into explicit evidence, responsibilities, and conditions, which improves release quality and reduces ambiguity during launch review.
