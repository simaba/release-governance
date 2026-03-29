# Usage Guide

This guide shows a simple way to use the repository as an operating framework rather than just a reading set.

## Recommended flow

1. Start with `docs/overview.md` for the core intent.
2. Use `docs/risk-model.md` to define the release risk inputs.
3. Use `docs/gating-matrix.md` to determine the minimum controls required for the resulting tier.
4. Use `docs/accountability-raci.md` to assign decision rights and operational ownership.
5. Use the templates in `templates/` to prepare the release evidence package.
6. Use `src/governance_cli.py` with a JSON profile in `examples/` to generate a simple release decision report.
7. Use `docs/worked-example-ivi-assistant.md` as a reference pattern for real deployments.
8. Use `docs/standards-mapping.md` when translating the framework for audit, governance, or stakeholder review.

## Example command

From the `src/` directory:

```bash
python governance_cli.py ../examples/ivi_voice_assistant_release_profile.json --format text
```

Example JSON output:

```bash
python governance_cli.py ../examples/ivi_voice_assistant_release_profile.json --format json
```

## Suggested review package

A lightweight release package can contain:
- release readiness checklist,
- risk score and tier,
- list of required gates,
- evidence links,
- accountability map,
- post-release monitoring plan,
- incident response playbook.

## How to extend the framework

Teams can extend this repository by:
- adjusting the risk dimensions,
- changing threshold logic,
- adding domain-specific gate requirements,
- linking reviewer sets to internal governance boards,
- integrating the CLI into a broader delivery workflow.
