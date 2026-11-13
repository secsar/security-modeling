# Choose a model by the property

A model is useful when its abstractions match the property you need. One model rarely answers every security question.

| Question | Model structure | Property | Important refinement gap |
| --- | --- | --- | --- |
| Who may access an object? | Access matrix, role or attribute predicates | Every allowed request satisfies policy | Identity and attribute provenance |
| Who may delegate authority? | Administrative transitions and capability relationships | Authority changes preserve delegation constraints | In-flight requests and caches |
| Where may information flow? | Labels, dominance, explicit release | Ordinary flows use allowed destinations | Timing and indirect observations |
| Can approved content change unnoticed? | Versions and approval state machine | Approval identifies the current version | Concurrent updates and atomicity |
| Must approval involve another person? | Identity-aware separation of duties | Required actors differ per transaction | Shared identities and admin bypass |
| Can a service recover within a deadline? | Failure, capacity, time, recovery states | Progress under explicitly stated failures | Scheduling and external dependencies |
| Does code implement the abstract rule? | Refinement mapping | Concrete behavior conforms to specified behavior | Extra interfaces and privileged paths |

## Composition

Authorization can establish who may read, lifecycle rules which version is approved, and information-flow rules where derived information goes. Check the boundaries between them: an authorized worker or export path can bypass a restriction enforced only on direct user reads.

A sequential atomic model also needs a refinement argument before it describes a concurrent implementation.

## Formality

| Form | Useful output | Overclaim to avoid |
| --- | --- | --- |
| Prose and tables | Shared definitions and reviewable decisions | Calling a diagram a proof |
| Mathematical specification | Precise predicates and obligations | Assuming notation validates assumptions |
| Executable model | Reproducible decisions and counterexamples | Treating a model as production enforcement |
| Finite-state exploration | Complete exploration within stated bounds | Generalizing to unbounded states or time |
| Mechanized proof | Checked theorem under formal assumptions | Claiming correctness of unmodeled code |

The [labs](../docs/labs.md) occupy the executable/finite exploration levels. The service case study remains semi-formal.

[NIST SP 800-192](https://csrc.nist.gov/pubs/sp/800/192/final) discusses access-control policy/model verification and implementation testing. [NIST IR 8539](https://csrc.nist.gov/pubs/ir/8539/final) discusses security-property verification through transition models. The labs do not claim to implement either publication's complete methods.
