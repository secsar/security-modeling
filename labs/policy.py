"""Small policy-decision model. Identity and attributes are assumed authoritative."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Subject:
    name: str
    memberships: frozenset[tuple[str, str]]
    active: bool = True


@dataclass(frozen=True)
class Document:
    tenant: str
    version: int
    approved_version: int | None
    state: str


@dataclass(frozen=True)
class Decision:
    permitted: bool
    reason: str


def decide(subject: Subject | None, action: str, document: Document | None) -> Decision:
    """Evaluate one snapshot; roles do not imply other roles. Unknowns deny."""
    if subject is None or not subject.active:
        return Decision(False, "identity_missing_or_inactive")
    if document is None or not document.tenant:
        return Decision(False, "object_missing_or_invalid")
    if document.state not in {"quarantined", "approved", "retired"}:
        return Decision(False, "unknown_lifecycle_state")
    if document.version < 1:
        return Decision(False, "invalid_version")
    if action not in {"read", "replace", "retire"}:
        return Decision(False, "unknown_action")
    role = "reader" if action == "read" else "editor"
    if (document.tenant, role) not in subject.memberships:
        return Decision(False, "tenant_role_required")
    if action == "read":
        if document.state != "approved" or document.approved_version != document.version:
            return Decision(False, "current_version_not_approved")
    elif document.state == "retired":
        return Decision(False, "retired_is_terminal")
    return Decision(True, "policy_satisfied")
