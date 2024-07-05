from collections import Counter
from typing import List, Tuple, Dict


def rate_similarity(a: Tuple[str], b: Tuple[str]) -> float:
    """
    Computes the similarity between two tuples using Jaccard
    index: It converts the tuples to sets, calculates the
    intersection and union, and then divides the size of it by
    the size of the union.
    """
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return float(len(intersection)) / len(union) if len(union) != 0 else 0


def evaluate_duplicates(
    data: List[Tuple[str]], threshold: float
) -> Dict[Tuple[str], List[Tuple[str]]]:
    """
    This function takes a list of tuples (data) and a similarity
    threshold (threshold). It compares each pair of tuples,
    calculates their similarity, and if the similarity is above
    the threshold, it considers them as possible duplicates.
    """
    duplicates = {}
    for i, tuple_a in enumerate(data):
        for j, tuple_b in enumerate(data):
            if i < j:
                similarity = rate_similarity(tuple_a, tuple_b)
                if similarity >= threshold:
                    if tuple_a not in duplicates:
                        duplicates[tuple_a] = []
                    duplicates[tuple_a].append((tuple_b, similarity))
    return duplicates


if __name__ == "__main__":
    data = [
        ("a", "b", "c"),
        ("a", "b", "d"),
        ("e", "f", "g"),
        ("a", "b", "c", "d"),
        ("h", "i", "j"),
        ("a", "c", "d"),
    ]

    threshold = 0.5
    duplicates = evaluate_duplicates(data, threshold)
    for key, value in duplicates.items():
        print(f"Possible duplicates for {key}:")
        for v in value:
            print(f"\t{v[0]} with similarity {v[1]:.2f}")
