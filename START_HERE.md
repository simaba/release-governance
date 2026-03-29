# Start Here

This repository is a lightweight but operational framework for releasing AI-enabled features in regulated or safety-critical environments.

It is designed to answer a practical question:

**How should a team decide whether an AI-enabled feature is truly ready to launch?**

## What this repository now contains

### Core framework
- `docs/overview.md`
- `docs/risk-model.md`
- `docs/release-gates.md`
- `docs/accountability.md`

### Operational artifacts
- `docs/gating-matrix.md`
- `docs/accountability-raci.md`
- `docs/standards-mapping.md`
- `docs/usage-guide.md`

### Worked example
- `docs/worked-example-ivi-assistant.md`

### Templates
- `templates/release-readiness-checklist.md`
- `templates/incident-response-template.md`
- `templates/post-release-monitoring-plan.md`

### Reference code
- `src/risk_scoring.py`
- `src/gate_policy.py`
- `src/governance_cli.py`

### Example input
- `examples/ivi_voice_assistant_release_profile.json`
- `examples/high_risk_adas_release_profile.json`

## Fastest way to understand the repo

1. Read `docs/overview.md`
2. Read `docs/gating-matrix.md`
3. Read `docs/worked-example-ivi-assistant.md`
4. Review `docs/accountability-raci.md`
5. Run the CLI on an example profile

## Example command

From the `src/` directory:

```bash
python governance_cli.py ../examples/ivi_voice_assistant_release_profile.json --format text
```

## Positioning

This is not a compliance template and not employer-specific material.
It is a documentation-first governance framework with lightweight reference code for:
- risk-tiered release decisions,
- fallback and degraded-mode expectations,
- observability and post-release control,
- accountability design for human oversight.

## Intended audience

This repository is most relevant for teams working on:
- automotive software,
- safety-adjacent AI systems,
- regulated digital products,
- operational governance for AI-enabled features.
