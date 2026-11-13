# Access-control models

## Core vocabulary

Let S be subjects, O objects, and A actions. An access-control matrix M assigns a set of rights to each subject–object pair:

M[s,o] ⊆ A.

Authorization requires the requested action to belong to that set. The matrix describes rights; it does not determine who may grant them, how revocation works, or how concurrent operations observe changes. Those require administrative and state rules.

## Role-based specification

Let R be roles, UA ⊆ S × R user–role assignments, and PA ⊆ R × A × O permission assignments. With active roles AR(s) restricted to assigned roles:

Permit(s,a,o) ⇔ ∃r ∈ AR(s): (r,a,o) ∈ PA.

This is a simplified model without role hierarchy. If hierarchy is added, specify inheritance direction and closure. Separate static separation of duties (forbidden assignments) from dynamic separation of duties (forbidden simultaneous activations).

Example constraint: a payment requester must not approve the same payment. Role separation alone may be insufficient: the policy must also compare the requesting and approving subject identities for that transaction.

## Attribute-based specification

An ABAC decision evaluates subject, object, action, and relevant environment attributes against policy. For example:

Permit(s,read,o,e) ⇔ Active(s) ∧ Member(s,Tenant(o)) ∧ Reader(s,Tenant(o)) ∧ State(o)=approved.

Specify:
- Attribute authority and update rules.
- Missing and malformed attribute behavior.
- Evaluation time and cache lifetime.
- Combining behavior for overlapping rules.
- Who can alter memberships and policy.
- Whether a failed lookup produces denial or another explicit result.

In this repository's example, missing attributes deny access and all required conditions must hold. This is a local policy choice, not a universal ABAC rule.

## Administrative policy

Permission to manage memberships must not imply permission to read content. Model assignment, revocation, and role changes as explicit transitions. Constrain self-granting, cross-domain grants, and the last remaining administrator where applicable.

## Questions for model review

Can a subject accumulate conflicting permissions? Does a parent role inherit unintended rights? Can a policy editor bypass its own constraints? Does revocation affect new operations, open sessions, or already-issued capabilities?

References: [NIST RBAC and ABAC publications](../docs/references.md). These examples are simplified specifications, not implementations of a complete standard.
