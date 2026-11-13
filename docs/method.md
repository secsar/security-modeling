# Security modeling method

## 1. Define protection requirements

Describe the system purpose and properties stakeholders need: confidentiality, integrity, authorized use, accountability, or service continuity. Assign requirement IDs. Express requirements as observable conditions where possible.

Example: R-01 — a human user may read only approved documents belonging to an organization in which that user currently holds a reader role.

## 2. Define the model universe

Specify subjects S, objects O, actions A, environment E, state space Σ, initial states Init, and transition relation T. State which values are authoritative, how unknown values are treated, and which operations are excluded.

A model need not use a theorem prover to be useful. Label prose and mathematical specifications accurately as semi-formal when syntax and semantics are not fully mechanized.

## 3. Specify policy

Define Permit(s, a, o, e, σ). Identify deny defaults, rule-combination behavior, administrative authority, and revocation semantics. Describe policy updates as carefully as content operations.

Separate authentication assumptions from authorization decisions. A successful login identifies a subject; the policy determines allowed operations.

## 4. State security properties

An invariant I is intended to hold in every reachable state. A transition property constrains a step from σ to σ′. A trace property constrains a sequence of steps; some information-flow properties compare multiple executions.

Do not turn every goal into an invariant by name alone. Eventual completion is a liveness property and requires progress assumptions.

## 5. Model transitions

For each action specify actor, precondition, changed fields, unchanged fields, and result. Explicit frame conditions prevent an apparently narrow operation from silently modifying security labels or ownership.

Specify atomicity and concurrency assumptions. If authorization and data access can observe different states, model that interval or identify it as an unresolved refinement obligation.

## 6. Allocate enforcement

Map each rule to the component that enforces it and the authoritative data it uses. Identify the trusted computing base: components whose incorrect behavior can invalidate the model.

Record bypass paths, administrative operations, caches, background workers, and exported capabilities. The model's scope must match its assurance claim.

## 7. Establish assurance obligations

For an invariant, show:
- Initialization: every permitted initial state satisfies I.
- Preservation: every permitted transition from an I-state produces another I-state.

Then determine how the implementation corresponds to the modeled states and actions. Use [assurance guidance](assurance.md) to distinguish planned evidence from completed work.

## 8. Review sufficiency and change

Verification asks whether the model satisfies specified properties; validation asks whether those properties represent the intended protection needs. Revisit both when requirements, policy administration, concurrency, trust dependencies, or external interfaces change.

Use the [template](../templates/security-model.md) to record the complete specification.
