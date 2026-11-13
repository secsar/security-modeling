"""Finite approval workflow with explicit state exploration and a known mutant."""
from collections import deque
from dataclasses import asdict, dataclass, replace


@dataclass(frozen=True)
class State:
    status: str = "draft"
    version: int = 1
    approved_version: int | None = None
    author: str = "alice"
    approver: str | None = None


@dataclass(frozen=True)
class Action:
    name: str
    actor: str


# Fixed role relation: both users can approve, but authors cannot approve their own work.
APPROVERS = frozenset({"alice", "bob"})
CUSTODIANS = frozenset({"bob"})
ACTIONS = tuple(Action(name, actor) for name in ("submit", "approve", "revise", "retire")
                for actor in ("alice", "bob"))


def transition(state: State, action: Action, *, max_version: int = 3,
               stale_approval_mutant: bool = False) -> State | None:
    """Return a new state or None for a denied transition. Input is immutable.

    max_version is an exploration bound, not a production policy.
    stale_approval_mutant intentionally demonstrates an incorrect revise transition.
    """
    if action.name == "submit" and action.actor == state.author and state.status == "draft":
        return replace(state, status="submitted")
    if (action.name == "approve" and action.actor in APPROVERS
            and action.actor != state.author and state.status == "submitted"):
        return replace(state, status="approved", approver=action.actor,
                       approved_version=state.version)
    if (action.name == "revise" and action.actor == state.author
            and state.status in {"draft", "submitted", "approved"}
            and state.version < max_version):
        if stale_approval_mutant and state.status == "approved":
            return replace(state, version=state.version + 1)
        return replace(state, status="draft", version=state.version + 1,
                       approver=None, approved_version=None)
    if action.name == "retire" and action.actor in CUSTODIANS and state.status == "approved":
        return replace(state, status="retired")
    return None


def state_violations(state: State) -> list[str]:
    errors = []
    if state.status == "approved":
        if state.approver is None or state.approver == state.author:
            errors.append("I-01: approval requires a different person")
        if state.approved_version != state.version:
            errors.append("I-02: approval must match current version")
    return errors


def step_violations(before: State, action: Action, after: State) -> list[str]:
    errors = []
    if before.author != after.author:
        errors.append("F-01: author is immutable")
    if before.status == "retired":
        errors.append("I-04: retired state has no outgoing transitions")
    if action.name == "revise" and (after.status != "draft"
            or after.approver is not None or after.approved_version is not None):
        errors.append("I-03: revision clears approval and returns to draft")
    return errors


def explore(max_version: int = 3, *, stale_approval_mutant: bool = False) -> dict:
    """Breadth-first exploration to closure within a finite version bound.

    This is executable finite-state enumeration, not an unbounded proof. Read paths,
    storage, role changes, concurrency, time and liveness are not represented.
    """
    if not 1 <= max_version <= 50:
        raise ValueError("max_version must be between 1 and 50")
    initial = State()
    queue = deque([(initial, [])])
    seen = {initial}
    accepted = denied = 0
    while queue:
        before, trace = queue.popleft()
        for action in ACTIONS:
            after = transition(before, action, max_version=max_version,
                               stale_approval_mutant=stale_approval_mutant)
            if after is None:
                denied += 1
                continue
            accepted += 1
            next_trace = trace + [{"action": asdict(action), "after": asdict(after)}]
            errors = state_violations(after) + step_violations(before, action, after)
            if errors:
                return {"model": "approval-workflow", "max_version": max_version,
                        "mutant": stale_approval_mutant, "explored_states": len(seen),
                        "accepted_transitions": accepted, "denied_attempts": denied,
                        "complete": False, "violations": errors,
                        "initial": asdict(initial), "counterexample": next_trace}
            if after not in seen:
                seen.add(after)
                queue.append((after, next_trace))
    return {"model": "approval-workflow", "max_version": max_version,
            "mutant": stale_approval_mutant, "explored_states": len(seen),
            "accepted_transitions": accepted, "denied_attempts": denied,
            "complete": True, "violations": [], "counterexample": []}
