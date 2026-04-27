# Release Governance vs. Release Checklist

These two repositories are intentionally related, but they solve different problems.

## Short version

| Repository | Primary purpose | Artifact type |
|---|---|---|
| [`release-governance`](https://github.com/simaba/release-governance) | Define the release lifecycle, gate expectations, and decision model | Framework + review artifacts |
| [`release-checklist`](https://github.com/simaba/release-checklist) | Validate structured readiness configuration from the command line | CLI tool + YAML configs |

## Use `release-governance` when

You need to answer lifecycle and decision questions:

- Which release stage are we in?
- Which gates apply at this stage?
- Who needs to approve?
- What evidence is required?
- What conditions block release?
- What monitoring or rollback expectations apply after release?

Typical outputs:

- release gate review
- stage-specific approval criteria
- open-risk and condition list
- rollout and rollback plan
- decision log and sign-off structure

## Use `release-checklist` when

You need repeatable validation:

- Is the YAML release-readiness file structurally valid?
- Are required fields present?
- Are required gates passed for the chosen risk tier?
- Can this be checked in CI before deployment?
- Can the output be rendered as text, JSON, or Markdown?

Typical outputs:

- validation result
- failed gate list
- machine-readable JSON report
- CI pass/fail signal

## Recommended workflow

1. Use `release-governance` to define the lifecycle stage, evidence expectations, and sign-off model.
2. Translate the gate requirements into a `release-checklist` YAML configuration.
3. Run `release-checklist validate` locally and in CI.
4. Attach the checklist report to the release gate review.
5. Record final decision, conditions, and follow-up review date in the release gate artifact.

## Why keep them separate?

Keeping the framework and CLI separate avoids mixing two different concerns:

- governance judgment: what should be required, who approves, and why
- validation automation: whether the structured readiness artifact passes defined rules

The separation keeps each repo easier to understand, test, and reuse.
