import unittest
from dataclasses import replace
from labs.flow import Label, can_flow, check_lattice, join
from labs.policy import Document, Subject, decide
from labs.workflow import Action, State, explore, state_violations, transition


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.reader = Subject("alice", frozenset({("A", "reader")}))
        self.doc = Document("A", 1, 1, "approved")

    def test_authorized_read(self):
        self.assertTrue(decide(self.reader, "read", self.doc).permitted)

    def test_cross_tenant_denial(self):
        self.assertFalse(decide(self.reader, "read", replace(self.doc, tenant="B")).permitted)

    def test_revocation_applies_to_next_snapshot(self):
        self.assertTrue(decide(self.reader, "read", self.doc).permitted)
        revoked = replace(self.reader, memberships=frozenset())
        self.assertFalse(decide(revoked, "read", self.doc).permitted)

    def test_admin_does_not_imply_reader(self):
        admin = Subject("admin", frozenset({("A", "membership_admin")}))
        self.assertFalse(decide(admin, "read", self.doc).permitted)

    def test_editor_cannot_read_but_can_replace(self):
        editor = Subject("editor", frozenset({("A", "editor")}))
        self.assertFalse(decide(editor, "read", self.doc).permitted)
        self.assertTrue(decide(editor, "replace", self.doc).permitted)

    def test_stale_approval_denied(self):
        self.assertFalse(decide(self.reader, "read", replace(self.doc, version=2)).permitted)

    def test_unknowns_and_inactive_deny(self):
        cases = [(None, "read", self.doc), (self.reader, "read", None),
                 (self.reader, "delete", self.doc),
                 (replace(self.reader, active=False), "read", self.doc),
                 (self.reader, "read", replace(self.doc, state="unexpected"))]
        for subject, action, document in cases:
            with self.subTest(action=action, document=document):
                self.assertFalse(decide(subject, action, document).permitted)

    def test_retired_is_terminal(self):
        editor = Subject("editor", frozenset({("A", "editor")}))
        self.assertFalse(decide(editor, "replace", replace(self.doc, state="retired")).permitted)


class FlowTests(unittest.TestCase):
    def test_confidentiality_direction(self):
        low, high = Label(0, frozenset()), Label(2, frozenset({"Finance"}))
        self.assertTrue(can_flow(low, high))
        self.assertFalse(can_flow(high, low))

    def test_categories_are_not_interchangeable(self):
        self.assertFalse(can_flow(Label(1, frozenset({"Finance"})),
                                  Label(2, frozenset({"Research"}))))

    def test_join_carries_both_dependencies(self):
        self.assertEqual(join(Label(1, frozenset({"Finance"})), Label(2, frozenset({"Research"}))),
                         Label(2, frozenset({"Finance", "Research"})))

    def test_complete_declared_domain(self):
        self.assertEqual(check_lattice(), {"labels": 12, "ordered_pairs": 144,
                                          "ordered_triples": 1728, "violations": 0})

    def test_invalid_level_rejected(self):
        with self.assertRaises(ValueError):
            Label(3, frozenset())


class WorkflowTests(unittest.TestCase):
    def approved(self):
        submitted = transition(State(), Action("submit", "alice"))
        return transition(submitted, Action("approve", "bob"))

    def test_author_cannot_self_approve_even_with_role(self):
        submitted = transition(State(), Action("submit", "alice"))
        self.assertIsNone(transition(submitted, Action("approve", "alice")))

    def test_legitimate_workflow(self):
        approved = self.approved()
        self.assertEqual(approved.status, "approved")
        self.assertEqual(state_violations(approved), [])
        self.assertEqual(transition(approved, Action("retire", "bob")).status, "retired")

    def test_revision_removes_approval(self):
        changed = transition(self.approved(), Action("revise", "alice"))
        self.assertEqual((changed.status, changed.version, changed.approver, changed.approved_version),
                         ("draft", 2, None, None))

    def test_retired_state_has_no_outgoing_edges(self):
        retired = transition(self.approved(), Action("retire", "bob"))
        for name in ("submit", "approve", "revise", "retire"):
            for actor in ("alice", "bob"):
                self.assertIsNone(transition(retired, Action(name, actor)))

    def test_denied_action_does_not_mutate(self):
        before = State()
        self.assertIsNone(transition(before, Action("approve", "bob")))
        self.assertEqual(before, State())

    def test_finite_exploration_closes_without_violation(self):
        for bound in (1, 2, 3, 5):
            with self.subTest(bound=bound):
                result = explore(bound)
                self.assertTrue(result["complete"])
                self.assertEqual(result["violations"], [])
                self.assertEqual(result["explored_states"], 4 * bound)

    def test_checker_detects_known_bad_transition(self):
        result = explore(3, stale_approval_mutant=True)
        self.assertFalse(result["complete"])
        self.assertIn("I-02: approval must match current version", result["violations"])
        self.assertEqual([step["action"]["name"] for step in result["counterexample"]],
                         ["submit", "approve", "revise"])

    def test_bounds_are_explicit(self):
        self.assertFalse(explore(1, stale_approval_mutant=True)["counterexample"])
        with self.assertRaises(ValueError):
            explore(0)


if __name__ == "__main__":
    unittest.main()
