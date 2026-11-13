"""Run the offline demonstrations with python -m labs."""
import argparse
import json
import sys
from dataclasses import asdict
from .flow import check_lattice
from .policy import Document, Subject, decide
from .workflow import explore


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("policy", "flow", "workflow", "counterexample"))
    parser.add_argument("--max-version", type=int, default=3)
    args = parser.parse_args(argv)
    if args.command == "policy":
        document = Document("A", 1, 1, "approved")
        scenarios = {
            "tenant_reader": Subject("alice", frozenset({("A", "reader")})),
            "other_tenant": Subject("bob", frozenset({("B", "reader")})),
            "admin_without_reader": Subject("carol", frozenset({("A", "membership_admin")})),
            "revoked_reader": Subject("alice", frozenset()),
        }
        result = {name: asdict(decide(subject, "read", document))
                  for name, subject in scenarios.items()}
    elif args.command == "flow":
        result = check_lattice()
    else:
        try:
            result = explore(args.max_version, stale_approval_mutant=args.command == "counterexample")
        except ValueError as exc:
            parser.error(str(exc))
    print(json.dumps(result, indent=2))
    # A discovered counterexample is success for that demonstration, not for the mutant.
    if args.command == "counterexample":
        return 0 if result["counterexample"] else 1
    return 1 if result.get("violations") else 0


if __name__ == "__main__":
    sys.exit(main())
