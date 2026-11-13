# Executable labs

Run commands from the repository root with Python 3.10+. All examples are offline and use synthetic identities.

## Lab 1 — Authorization over state

Run `python3 -m labs policy`.

Expected: tenant reader allowed; reader in another tenant denied; administrator without reader permission denied; revoked reader denied. Reason codes explain model decisions; they are not production responses to expose to arbitrary callers.

The [policy module](../labs/policy.py) covers read, replace, and retire authorization over one snapshot. It does not implement storage or membership administration. Change membership and rerun to explore revocation. Roles are independent.

Identity validation, input validation, authoritative attribute loading, and atomic enforcement belong to an implementation refinement, not this in-memory model.

## Lab 2 — Information flow

Run `python3 -m labs flow`.

There are three levels and two optional compartments. A destination must dominate the source in both level and category inclusion. The join is the least label capable of receiving information from both inputs.

The [flow module](../labs/flow.py) enumerates 12 labels and checks reflexivity, antisymmetry, transitivity, and the join's least-upper-bound property. It does not model covert channels, declassification, trace-level noninterference, or integrity labels.

Exercise: add a compartment to `finite_labels`, predict the domain size, then rerun. Keep documented bounds aligned with the actual domain.

## Lab 3 — Explore an approval workflow

Run `python3 -m labs workflow --max-version 3`.

From a single draft, the explorer tries eight action/actor combinations per reachable state, until no unseen state remains. Denied operations produce no new state. Alice has author and approver capabilities; Bob is approver and custodian. Alice still cannot approve her own record.

The version bound limits the modeled universe, not a production revision policy. State deduplication checks state and step properties; it does not enumerate all history-dependent properties.

Checks: approving person differs from author, approval matches the current version, revision clears approval, retirement has no outgoing edge, and authorship remains immutable.

## Lab 4 — Detect a known defect

Run `python3 -m labs counterexample --max-version 3`.

An intentionally incorrect transition increments an approved record's version without clearing its approval. Breadth-first exploration returns a shortest trace: Alice submits, Bob approves, Alice revises. The final record is approved at version 2 with approval for version 1.

The command exits 0 when it finds the expected defect. That means the demonstration succeeded, not that the mutant is correct. With `--max-version 1`, revision is impossible, so it exits 1 without a counterexample: a bound can hide a defect.

## Relationship to the specifications

The workflow lab implements the separate [approval-workflow model](../models/state-and-integrity.md), not all of [SM-01](../case-studies/tenant-document-service.md). The policy lab illustrates a subset of SM-01 decisions.

Authentication, persistence, distributed caches, concurrent transactions, audit systems, and network behavior are not executed. Results are conditional on the model and its declared checks.

Run `python3 -m unittest discover -s tests -v` for valid workflows, denial behavior, role separation, revocation snapshots, label joins, exploration at several bounds, and known-defect detection. See the [validation record](validation.md).
