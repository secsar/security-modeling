# Scope and repository boundary

Terminology varies across security practice. This project adopts an explicit artifact boundary so security modeling and threat modeling remain organized.

| Dimension | Security modeling: this repository | Threat modeling: separate repository |
| --- | --- | --- |
| Main question | What does secure behavior mean, and which rules preserve it? | What can go wrong, through which adversarial or failure scenarios? |
| Primary entities | Subjects, objects, actions, attributes, labels, states | Threat actors, entry points, attack paths, weaknesses |
| Core output | Policy model, allowed transitions, invariants, assurance obligations | Threat scenarios, attack trees, prioritization, mitigation analysis |
| Review question | Is the specification consistent, sufficient, and correctly enforced? | Are relevant threats identified and appropriately addressed? |

These are complementary views, not mutually exclusive bodies of knowledge. A failed invariant may motivate a threat scenario; a threat finding may reveal a missing policy requirement.

## In scope

- Authorization and administrative policy models.
- Confidentiality and information-flow properties.
- Integrity, separation of duties, and constrained state transitions.
- Security domains, trusted components, and enforcement responsibilities.
- Availability and resilience properties when defined through explicit capacity, timing, or recovery assumptions.
- Formal and semi-formal specifications, refinement, and assurance evidence.

Access control is one part of security modeling, not its full extent.

## Outside this repository's primary scope

Threat catalogs, attack trees, attacker walkthroughs, likelihood/impact registers, vulnerability exploitation guides, and incident playbooks.

## Exchange contract

A cross-repository reference should identify the source artifact and version, the affected requirement or property, and the reason for the relationship. Keep the original artifact in its owning repository; do not duplicate a threat register here.

The companion [threat-modeling repository](https://github.com/secsar/threat-modeling) owns threat analysis. Use a commit-specific URL when relying on a particular model revision.

## Publication boundary

Use fictional systems, synthetic records, and public sources. Do not incorporate private business material, employer or customer architecture, internal project names, or confidential operational details.
