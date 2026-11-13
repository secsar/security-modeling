# Security Modeling
### Architecture • Threats • Risk • Assurance

A practical collection of security models, architecture decisions, and worked case studies maintained by **Stéphane Ikoué**.

Security modeling connects what a system does to what can go wrong, the decisions that reduce risk, and the evidence needed to trust those decisions.

## Start here

- **[Explore the first case study](case-studies/tenant-document-service.md):** protecting tenant boundaries in a document service.
- **[Use the modeling template](templates/security-model.md):** document scope, trust boundaries, threats, decisions, and verification.
- **[Follow the method](docs/method.md):** move from a system description to an actionable security review.

## What this repository covers

| Area | Questions |
| --- | --- |
| Security architecture | Where are trust boundaries, and which components enforce them? |
| Threat modeling | What could an attacker do, under which conditions? |
| Risk analysis | Which failures matter most, and why? |
| Security assurance | What evidence would demonstrate that controls work? |
| Design decisions | What tradeoffs remain, and who accepts them? |

## First case study

A fictional multi-tenant document service illustrates cross-tenant access, leaked download links, malicious uploads, privileged access, and resource exhaustion. Each threat connects to a proposed control and a concrete verification procedure.

**Status:** documentation baseline. The examples are design exercises; no deployed application, completed penetration test, or measured risk reduction is claimed.

## Approach

1. Describe the system and its business purpose.
2. Identify assets, identities, data flows, and trust boundaries.
3. Write specific threat scenarios.
4. Prioritize risks using explicit assumptions.
5. Record controls and architecture decisions.
6. Define verification evidence and review residual risk.

## About

Maintained by Stéphane Ikoué. Professional background and research: [StephSec](https://stephsec.com).

All systems, organizations, records, and scenarios in the examples are fictional. Contributions should contain original or appropriately attributed public material. See [contribution guidance](CONTRIBUTING.md).
