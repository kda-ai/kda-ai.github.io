"""
PC Member Assignment Tool
--------------------------
Assigns exactly 3 distinct PC members to each paper submitted to a workshop.
The assignment is balanced so that no single PC member is disproportionately
overloaded, and reviewer overlap between any two papers is minimized.
"""

import random
from itertools import combinations

# ── Configuration ─────────────────────────────────────────────────────────────

PC_MEMBERS = [
    "Aslak Johansen",
    "Jakob Hviid",
    "Francesco Daghero",
    "Sune Lundø Sørensen",
    "Matteo Esposito",
    "Alexander Bakhtin",
    "Klara Borowa",
]

PAPERS = [
    "214 CellFlow: A Tool For Automatic Jupyter Notebook Workflow Visualization",
    "215 A Cost-Effective Architecture for Enterprise LLM Applications: Balancing Competing Requirements through RAG-Augmented CPU-Only Inference",
    "307 An Efficient Approach for Model Recovery from Image Containing Diagrams",
    "321 CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models",
    "322 An Empirical Analysis of LLM-Driven Refactoring for Microservices",
]

REVIEWERS_PER_PAPER = 3


# ── Validation ────────────────────────────────────────────────────────────────


def validate_inputs(pc_members: list[str], papers: list[str], k: int) -> None:
    """Raises ValueError if the configuration is mathematically infeasible."""
    if len(pc_members) < k:
        raise ValueError(
            f"At least {k} PC members are required to assign {k} reviewers "
            f"per paper. Only {len(pc_members)} members were provided."
        )


# ── Assignment Algorithm ──────────────────────────────────────────────────────


def assign_reviewers(
    pc_members: list[str],
    papers: list[str],
    k: int = REVIEWERS_PER_PAPER,
    seed: int | None = 42,
    assignments: dict[str, list[str]] = {},
) -> dict[str, list[str]]:
    """
    Assigns k PC members to each paper using a load-balanced greedy strategy.

    Each PC member is selected based on the fewest assignments accumulated so
    far, so the review workload is distributed as evenly as possible. A
    tie-breaking shuffle is applied to avoid deterministic bias toward members
    who appear earlier in the list.

    Parameters
    ----------
    pc_members : list of reviewer names.
    papers     : list of paper titles.
    k          : number of reviewers required per paper.
    seed       : random seed for reproducibility (pass None for randomness).

    Returns
    -------
    A dictionary mapping each paper title to its list of assigned reviewers.
    """
    validate_inputs(pc_members, papers, k)

    rng = random.Random(seed)
    load: dict[str, int] = {member: 0 for member in pc_members}
    for paper, reviewers in assignments.items():
        for reviewer in reviewers:
            load[reviewer] += 1

    for paper in papers:
        if paper in assignments.keys():
            if len(assignments[paper]) == k:
                continue  # Skip papers that already have assigned reviewers.
        else:
            assignments[paper] = []

        # Sort members by current load; shuffle first to break ties randomly.
        candidates = pc_members[:]

        for candidate in assignments[paper]:
            candidates.remove(candidate)
        rng.shuffle(candidates)
        candidates.sort(key=lambda m: load[m])

        selected = candidates[:k-len(assignments[paper])]
        assignments[paper].extend(selected)

        for member in selected:
            load[member] += 1

    return assignments


# ── Reporting ─────────────────────────────────────────────────────────────────


def print_assignments(assignments: dict[str, list[str]]) -> None:
    """Prints the reviewer assignments in a readable tabular format."""
    print("\n" + "=" * 60)
    print("  REVIEWER ASSIGNMENTS")
    print("=" * 60)
    for paper, reviewers in assignments.items():
        print(f"\n  {paper}")
        for i, reviewer in enumerate(reviewers, start=1):
            print(f"    Reviewer {i}: {reviewer}")
    print("\n" + "=" * 60)


def print_load_summary(
    assignments: dict[str, list[str]], pc_members: list[str]
) -> None:
    """Prints how many papers are assigned to each PC member."""
    load: dict[str, int] = {m: 0 for m in pc_members}
    for reviewers in assignments.values():
        for reviewer in reviewers:
            load[reviewer] += 1

    print("\n  WORKLOAD SUMMARY")
    print("=" * 60)
    for member, count in sorted(load.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {member:<20} {bar}  ({count} paper(s))")
    print("=" * 60 + "\n")


def check_overlap(assignments: dict[str, list[str]]) -> None:
    """Reports the reviewer overlap count between every pair of papers."""
    print("\n  REVIEWER OVERLAP BETWEEN PAPER PAIRS")
    print("=" * 60)
    paper_list = list(assignments.keys())
    for p1, p2 in combinations(paper_list, 2):
        shared = set(assignments[p1]) & set(assignments[p2])
        overlap_count = len(shared)
        shared_str = ", ".join(shared) if shared else "none"
        print(
            f"  {p1[:30]:<32} ↔  {p2[:30]:<32}  overlap: {overlap_count}  ({shared_str})"
        )
    print("=" * 60 + "\n")


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":

    assignments: dict[str, list[str]] = {
        "321 CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models": [
            "Matteo Esposito",
            "Alexander Bakhtin",
            "Klara Borowa",
        ],
        "322 An Empirical Analysis of LLM-Driven Refactoring for Microservices": [
            "Matteo Esposito",
            "Alexander Bakhtin",
            "Klara Borowa",
        ],
        "214 CellFlow: A Tool For Automatic Jupyter Notebook Workflow Visualization": [
            "Sune Lundø Sørensen",
            "Jakob Hviid",
            "Francesco Daghero",
        ],
        "215 A Cost-Effective Architecture for Enterprise LLM Applications: Balancing Competing Requirements through RAG-Augmented CPU-Only Inference": [
            "Aslak Johansen",
            "Francesco Daghero",
            "Jakob Hviid",
        ],
        "307 An Efficient Approach for Model Recovery from Image Containing Diagrams": [
            "Sune Lundø Sørensen",
            "Aslak Johansen",
            "Matteo Esposito",
        ]
    }

    assignments = assign_reviewers(
        PC_MEMBERS, PAPERS, k=REVIEWERS_PER_PAPER, assignments=assignments
    )
    print_assignments(assignments)
    print_load_summary(assignments, PC_MEMBERS)
    # check_overlap(assignments)
