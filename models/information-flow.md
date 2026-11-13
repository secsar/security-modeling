# Information-flow models

Run `python3 -m labs flow` to execute the [finite label model](../labs/flow.py) corresponding to the ordinary-flow relation below. Its algebraic checks do not establish noninterference of an application.

Authorization answers whether an operation may occur. Information-flow modeling specifies where information may propagate, including through sequences of individually permitted operations.

## A small label model

For this illustrative confidentiality policy, labels are pairs (level, categories). Levels are ordered Public ≤ Internal ≤ Restricted. Categories are sets such as {Finance, Research}.

Define dominance:

(l₂,c₂) ⪰ (l₁,c₁) ⇔ l₂ ≥ l₁ ∧ c₂ ⊇ c₁.

An ordinary flow from source x to destination y is permitted only if Label(y) ⪰ Label(x). This prevents ordinary flows from a more restricted label to a less restrictive destination.

| Source | Destination | Ordinary flow |
| --- | --- | --- |
| Internal, {Finance} | Restricted, {Finance} | Allowed |
| Restricted, {Finance} | Internal, {Finance} | Denied |
| Internal, {Finance} | Restricted, {Research} | Denied |

These are rules for this toy model. They are not a complete implementation of a named mandatory-access-control model.

## Release and declassification

Some workflows need an explicitly authorized release to a lower label. Represent release as a separate transition with authority, purpose, input version, output transformation, and recorded decision. Do not silently exempt an ordinary copy operation.

A review of a summary does not authorize release of its source document. Bind approval to the exact released output.

## Observation and noninterference

A stronger property may require that changing secret inputs cannot change a public observer's visible outputs, except through authorized release. State exactly what the observer can see: values, errors, timing, sizes, or resource usage.

An access-control table alone does not establish that property. Comparing two executions also differs from checking one-state authorization predicates.

## Integrity is a separate dimension

Confidentiality labels do not establish data correctness or trusted provenance. Integrity models need their own ordering or workflow rules. Combining confidentiality and integrity constraints requires checking that legitimate workflows remain possible.

## Limits and assurance

This module specifies an illustrative label relation and discusses stronger properties; it contains no noninterference proof. Covert channels, timing behavior, and real release mechanisms require a more detailed model. See [assurance](../docs/assurance.md).
