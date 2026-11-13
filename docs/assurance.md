# Assurance and implementation refinement

## Traceability

Use stable IDs to connect each requirement to a policy, property, enforcing mechanism, and evidence artifact.

| Layer | Example |
| --- | --- |
| Requirement | R-01: approved content is readable only by current tenant readers |
| Policy | P-READ: membership, role, tenant, and lifecycle conditions all hold |
| Property | Authorized read events satisfy P-READ at their decision point |
| Mechanism | Server-side decision and object-version read within a consistent operation |
| Evidence | Model argument plus implementation tests and concurrency analysis |

## Evidence levels

| Evidence | Supports | Does not establish by itself |
| --- | --- | --- |
| Decision-table review | Agreement on listed cases | Behavior for all inputs |
| Unit or conformance tests | Observed behavior of tested cases | General correctness |
| Property-based testing | Broad sampled coverage under generators | Exhaustive coverage |
| Bounded model checking | Properties within the chosen finite bounds and semantics | Unbounded correctness |
| Formal proof | A theorem under stated definitions and assumptions | Correctness of unmodeled code or infrastructure |
| Implementation refinement argument | Correspondence between implementation and model | Adequacy of the original requirements |

## Proof obligations

For state invariant I:
1. Init(σ) ⇒ I(σ).
2. I(σ) ∧ T(σ,a,σ′) ⇒ I(σ′).

For authorization, show that each content-release event corresponds to an allowed model action. Include exceptional paths, workers, administrative reads, cached decisions, and exported links.

For information-flow claims, specify observation semantics and whether the argument compares states, steps, or complete executions.

## Refinement gaps

A model may treat authorization and reading as one atomic action while an implementation performs two separate operations. Identify the linearization point or synchronization mechanism that preserves the model's semantics.

A model may say revoked users cannot initiate reads, while an implementation issues transferable download links. Those links introduce new capabilities and must be modeled explicitly or excluded from the implementation.

## Evidence records

Record model version, implementation version, property IDs, method/tool version, assumptions, finite bounds if any, results, and unresolved limitations. Use states: Specified, Reviewed, Tested, or Proven with scope. Do not equate a planned test with evidence.

Primary reading: [NIST SP 800-192](https://csrc.nist.gov/pubs/sp/800/192/final). Its focus on policy/model verification and testing informs this repository's separation between specification and evidence.
