# Contributing

Contributions must develop security models: explicit policies, properties, state transitions, enforcement mappings, or assurance evidence.

Read the [scope boundary](docs/scope.md) before adding content. Threat scenarios, attack trees, and threat-prioritization registers belong in the separate threat-modeling repository.

## Required structure

Use the [specification template](templates/security-model.md). Define the model universe, assumptions, initial states, policy semantics, transitions, properties, and evidence status.

## Review criteria

For executable contributions, run `python3 -m unittest discover -s tests -v` and record the Python version and model bounds. Include permitted and denied cases, and a known defect that the checks detect where appropriate. Update the validation record only with observed results. Keep labs offline and dependency-free unless an additional tool materially improves the model.

- Are policy, model, and enforcement mechanism distinguished?
- Are subject and object attributes authoritative and well-defined?
- Are default decisions, administrative actions, and revocation explicit?
- Do transitions state preconditions, effects, and unchanged fields?
- Are invariants distinguished from trace, information-flow, and liveness properties?
- Are initialization, preservation, and implementation refinement addressed?
- Are evidence claims limited to work actually performed?
- Are legitimate permitted operations covered as well as denied operations?
- Do diagrams, tables, and definitions agree?
- Do links resolve and sources support their use?

Use fictional systems and synthetic data. Exclude private business details, employer or customer material, internal URLs, credentials, and personal records. Attribute public sources appropriately.

A pull request should explain the modeling problem, the resulting specification, and validation performed. Do not claim a proof, test result, or compliance status without reproducible supporting evidence.
