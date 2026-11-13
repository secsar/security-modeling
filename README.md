# Security Modeling
### Policies • Properties • State • Assurance

Security models specify the conditions under which a system is secure: who may act, which operations are permitted, how information may flow, and which properties must hold as state changes.

Maintained by **Stéphane Ikoué** · [StephSec](https://stephsec.com)

## Repository scope

This repository focuses on **security modeling**. Its core artifacts are policy specifications, subject–object relationships, state machines, security invariants, enforcement mappings, and assurance arguments.

Threat actors, attack trees, abuse cases, and threat prioritization belong in the separate threat-modeling repository. The two disciplines can exchange requirements and findings while retaining distinct artifacts. See the [scope and repository boundary](docs/scope.md).

## Explore

| Resource | Purpose |
| --- | --- |
| [Modeling method](docs/method.md) | Develop a model from protection requirements through assurance obligations |
| [Access-control models](models/access-control.md) | Specify roles, attributes, permissions, and administrative constraints |
| [Information-flow models](models/information-flow.md) | Define labels, allowed flows, and release rules |
| [State and integrity models](models/state-and-integrity.md) | Specify valid transitions, separation of duties, and invariants |
| [Assurance and refinement](docs/assurance.md) | Connect model properties to implementation evidence |
| [Worked document-service model](case-studies/tenant-document-service.md) | Follow one coherent model through policies, transitions, and assurance |
| [Reusable specification template](templates/security-model.md) | Start a new security model |
| [References](docs/references.md) | Primary sources and reading guide |

## Modeling principles

- Separate a **policy** (what must be allowed or prohibited), a **model** (its precise representation), and a **mechanism** (how it is enforced).
- Make assumptions, trust dependencies, and exclusions explicit.
- Define both permitted behavior and behavior that must be rejected.
- Check initial states and every modeled transition against stated invariants.
- Distinguish an explanatory argument, a test result, bounded model checking, and a general proof.
- Trace requirements to properties, enforcement points, and evidence.

## Current status

This is a documentation and specification foundation. The worked example is fictional and uses mathematical notation and decision tables. It is not a deployed service, executable policy engine, machine-checked proof, or compliance certification.

## Development sequence

1. Establish the security-modeling vocabulary and specification structure — included.
2. Specify access, information-flow, and state-integrity models — introductory modules included.
3. Develop a complete illustrative system model — document-service model included.
4. Add executable policy examples and conformance tests — planned.
5. Add bounded state exploration and publish reproducible evidence — planned.

Contributions follow the [repository scope and review criteria](CONTRIBUTING.md).
