# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] — Foundation release

### Added

- AI release lifecycle framework for staged governance decisions.
- Release gate review template for staging, production rollout, major model update, or retirement decisions.
- Filled generic sample release gate review artifact.
- Documentation clarifying the relationship between `release-governance` and `release-checklist`.
- README positioning that separates lifecycle governance from executable checklist validation.

### Notes

This repository defines release-stage governance expectations and decision artifacts. It should remain distinct from `release-checklist`, which provides executable YAML validation.

### Next

- Add stage-specific examples for pre-development, pre-deployment, deployment, post-deployment, and retirement.
- Add a release-condition tracker template.
- Add more examples of linking checklist reports to release gate decisions.
