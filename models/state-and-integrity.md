# State and integrity models

A state model defines valid security-relevant states and the operations that connect them.

## Illustrative approval workflow

A record has state, author, approver, content_version, and approved_version.

Allowed states: draft, submitted, approved, retired.

| Transition | Preconditions | Effects |
| --- | --- | --- |
| Submit | Actor is author; state=draft | state=submitted |
| Approve | Actor has approver role; actor≠author; state=submitted | state=approved; approver=actor; approved_version=content_version |
| Revise | Actor is author; state is draft, submitted, or approved | Increment content_version; state=draft; clear approver and approved_version |
| Retire | Actor has custodian role; state=approved | state=retired |

All unlisted operations are denied. Fields not named in effects are unchanged. Administrative role assignment is outside this small model and must be constrained in a full system.

## Integrity properties

- I-01: approved ⇒ approver≠author.
- I-02: approved ⇒ approved_version=content_version.
- I-03: every modeled content change returns the record to draft and removes approval.
- I-04: retired records have no outgoing transition in this model.

I-03 is a transition property; I-04 concerns the defined transition relation. They should not be confused with purely one-state predicates.

## Preservation reasoning

Approving a submitted record establishes I-01 through the actor inequality and I-02 through the version assignment. Revising an approved record invalidates approval, so the new content cannot retain the old approved state. A concurrent implementation must enforce these preconditions and effects atomically or supply an equivalent concurrency argument.

This is an explanatory argument, not a machine-checked proof.

## Availability and progress

“Every submitted record is eventually reviewed” is a liveness requirement. It does not follow from the integrity properties. It needs assumptions about available reviewers, scheduling, failures, and retries.

If a service must recover within a deadline, specify the failure model, recovery states, clock assumptions, capacity constraints, and measurable bound. A diagram alone cannot establish that guarantee.
