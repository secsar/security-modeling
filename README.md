# Security Modeling
### Specify secure behavior. Execute the model. Examine the evidence.

An educational security-modeling workbench maintained by **Stéphane Ikoué** · [StephSec](https://stephsec.com)

Turn security requirements into explicit policies, information-flow rules, state transitions, and properties that can be examined. This repository combines specifications with executable models and transparent verification limits.

## Run a model in two minutes

Requires Python 3.10+. No API key, cloud account, package installation, or network connection is required after obtaining the files.

```bash
git clone https://github.com/secsar/security-modeling.git
cd security-modeling
python3 -m labs policy
python3 -m labs flow
python3 -m labs workflow
python3 -m labs counterexample
python3 -m unittest discover -s tests -v
```

On Windows, use `py -3` in place of `python3` if needed. Run from the repository root. Commands print JSON and do not contact a service or write to a system under test.

## What is runnable?

| Lab | Learn by running | Evidence produced |
| --- | --- | --- |
| [Tenant authorization](labs/policy.py) | Distinguish a reader, another tenant, an administrator, and a revoked reader | Allow/deny decisions with reason codes |
| [Confidentiality labels](labs/flow.py) | Combine levels and compartments; compute a least upper bound | Exhaustive checks over 12 labels, 144 pairs, and 1,728 triples |
| [Approval workflow](labs/workflow.py) | Separate author and approver; invalidate approval when content changes | Reachable states and transitions within a version bound |
| [Counterexample](docs/labs.md) | Observe an intentionally incorrect revision transition | A shortest three-step trace to stale approval |

The default correct workflow explores **12 states and 15 accepted transitions**, with no violations of its declared checks. The mutant shows why “approved once” is insufficient: submit → approve → revise leaves version 2 carrying version 1's approval. These are results of finite educational models, not claims about a production system.

## Choose a path

| Goal | Start with |
| --- | --- |
| Choose a model for a requirement | [Model selection guide](models/model-selection.md) |
| Run and modify the labs | [Lab guide and coverage limits](docs/labs.md) |
| Write a model from scratch | [Method](docs/method.md) and [specification template](templates/security-model.md) |
| Study a semi-formal system specification | [Tenant document service](case-studies/tenant-document-service.md) |
| Connect a claim to evidence | [Assurance and refinement](docs/assurance.md) |
| Review actual verification results | [Validation record](docs/validation.md) |

## Core topics

- [Access control](models/access-control.md): identities, roles, attributes, and administrative authority.
- [Information flow](models/information-flow.md): confidentiality labels, propagation, and release rules.
- [State and integrity](models/state-and-integrity.md): valid transitions, separation of duties, and version-bound approval.
- [Primary references](docs/references.md): sources for deeper study.

## Keep the disciplines distinct

This repository owns **policies, permitted behavior, security properties, and assurance obligations**. The companion [threat-modeling repository](https://github.com/secsar/threat-modeling) owns scenarios, attack paths, and prioritization. [StephSec Research](https://github.com/secsar/stephsec-research) develops research questions and synthesis. See the [scope boundary](docs/scope.md).

## Maturity and limits

Included: executable educational labs, 21 tests, a finite-state explorer, a known failing model, and a semi-formal service specification. The Python models are deliberately small and operate on trusted in-memory inputs. They are not production authorization middleware. There is no unbounded proof, liveness analysis, concurrency verification, noninterference proof, or compliance certification.

Next: extend administrative policy, add implementation-refinement exercises, and compare richer formal specifications against the finite labs. Contributions must preserve explicit assumptions and evidence limits; see [CONTRIBUTING.md](CONTRIBUTING.md).
