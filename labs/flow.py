"""Finite confidentiality-label lattice; ordinary flow only, no declassification."""
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Label:
    level: int
    categories: frozenset[str]

    def __post_init__(self):
        if self.level not in {0, 1, 2}:
            raise ValueError("level must be 0 (Public), 1 (Internal), or 2 (Restricted)")


def dominates(destination: Label, source: Label) -> bool:
    return destination.level >= source.level and destination.categories >= source.categories


def can_flow(source: Label, destination: Label) -> bool:
    return dominates(destination, source)


def join(left: Label, right: Label) -> Label:
    """Least label that can receive information from both inputs."""
    return Label(max(left.level, right.level), left.categories | right.categories)


def finite_labels() -> tuple[Label, ...]:
    cats = ("Finance", "Research")
    subsets = [frozenset(c) for n in range(3) for c in combinations(cats, n)]
    return tuple(Label(level, subset) for level in range(3) for subset in subsets)


def check_lattice() -> dict:
    """Enumerate the entire 12-label domain and check stated algebraic properties."""
    def require(condition, property_name):
        if not condition:
            raise AssertionError(property_name)

    labels = finite_labels()
    for a in labels:
        require(dominates(a, a), "reflexivity")
        for b in labels:
            if dominates(a, b) and dominates(b, a):
                require(a == b, "antisymmetry")
            j = join(a, b)
            require(dominates(j, a) and dominates(j, b), "join upper bound")
            for c in labels:
                if dominates(a, b) and dominates(b, c):
                    require(dominates(a, c), "transitivity")
                if dominates(c, a) and dominates(c, b):
                    require(dominates(c, j), "join least upper bound")
    return {"labels": len(labels), "ordered_pairs": len(labels) ** 2,
            "ordered_triples": len(labels) ** 3, "violations": 0}
