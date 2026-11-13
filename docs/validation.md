# Validation record

**Date:** 2026-11-13  
**Environment:** Python 3.12.14, standard library only  
**Scope:** included educational models and tests; no deployed service

## Reproduce

```bash
python3 -m unittest discover -s tests -v
python3 -m labs policy
python3 -m labs flow
python3 -m labs workflow --max-version 3
python3 -m labs counterexample --max-version 3
```

## Observed results

| Check | Result | Scope |
| --- | --- | --- |
| Test suite | 21 passed | Named cases and exploration at version bounds 1, 2, 3, 5 |
| Authorization demonstration | One permit; three denials | Four declared snapshots |
| Label algebra | No assertion failures | 12 labels, 144 pairs, 1,728 triples |
| Correct workflow | 12 states; 15 accepted transitions; 81 denied attempts; no violations | Two users, fixed roles, one record, versions 1–3 |
| Known incorrect workflow | Counterexample: submit → approve → revise | Stale approval violates I-02 and I-03 |

The incorrect model is deliberately included to check that validation detects a known bad transition. This is not a discovered vulnerability in a real system.

## Limits

- Tests and exploration share Python code; a missing check can hide a defect.
- Fixed actors, roles, initial state, and version bounds limit the result.
- Persistence, concurrency, cryptography, infrastructure, and runtime enforcement were not evaluated.
- No liveness, noninterference, or general theorem was proved.
- Python 3.10+ is the intended syntax range; execution was observed on the environment above, not a full version/OS matrix.

This is a reproducible local validation record, not external assessment or certification.
