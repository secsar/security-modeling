# Security modeling method

This is the working method for this repository, not a certification or a claim of compliance with a particular framework.

## 1. Establish scope

Name the business service, system owner, users, sensitive assets, assumptions, and exclusions. Define the failure that matters to the business before selecting controls.

## 2. Model trust

Draw components and labeled data flows. Mark where data crosses a change in ownership, identity, privilege, or execution environment. Identify the enforcement point for each boundary. Authentication alone does not establish permission to access an object.

## 3. Describe threats

Use this form:

> An actor with [capability] can [action] through [entry point] because [weakness or assumption], causing [business consequence].

Consider identity abuse, data modification, unauthorized disclosure, loss of accountability, service disruption, and privilege escalation. Record preconditions and distinguish plausible scenarios from verified vulnerabilities.

## 4. Prioritize transparently

Use qualitative judgments, not invented numerical precision.

| Dimension | Low | Medium | High |
| --- | --- | --- | --- |
| Likelihood | Requires unusual access or several difficult preconditions | Feasible for an authenticated user or under a plausible failure | Accessible and repeatable with few preconditions |
| Impact | Limited, reversible disruption with little sensitive exposure | Material impact to one tenant or business process | Broad sensitive exposure, privileged compromise, or sustained critical outage |

For this repository: High impact with Medium or High likelihood is High priority; Low impact with Low likelihood is Low priority; other combinations are Medium. Review context before adopting this convention elsewhere.

Rate the **baseline scenario before the proposed controls**. Describe expected residual exposure separately. Do not lower an assessed rating solely because a control is planned.

## 5. Make decisions

Record the selected control, rejected alternatives, operational cost, owner role, and conditions that would trigger reconsideration. A useful decision explains why the control fits the system.

## 6. Define evidence

Give each threat a verification ID. Specify the setup, action, expected outcome, and evidence to retain. Include negative tests, such as requesting an object owned by another tenant.

Use explicit states: Planned, Implemented, Verified, or Accepted. Acceptance requires a named accountable owner and review date in a real implementation.

## 7. Revisit

Review when identities, data sensitivity, integrations, deployment boundaries, or business requirements change. Also revisit after incidents and failed verification.
