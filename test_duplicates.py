import unittest
from typing import List, Tuple, Dict


def rate_similarity(a: Tuple[str], b: Tuple[str]) -> float:
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return float(len(intersection)) / len(union) if len(union) != 0 else 0


def evaluate_duplicates(
    data: List[Tuple[str]], threshold: float
) -> Dict[Tuple[str], List[Tuple[Tuple[str], float]]]:
    duplicates = {}
    for i, tuple_a in enumerate(data):
        for j, tuple_b in enumerate(data):
            if i < j:  # Compare each pair only once
                similarity = rate_similarity(tuple_a, tuple_b)
                if similarity >= threshold:
                    if tuple_a not in duplicates:
                        duplicates[tuple_a] = []
                    duplicates[tuple_a].append((tuple_b, similarity))
    return duplicates


class TestEvaluateDuplicates(unittest.TestCase):

    def test_no_duplicates(self):
        data = [("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i")]
        threshold = 0.5
        expected_output = {}

        result = evaluate_duplicates(data, threshold)
        self.assertEqual(result, expected_output)

    def test_with_duplicates(self):
        data = [
            ("a", "b", "c"),
            ("a", "b", "d"),
            ("e", "f", "g"),
            ("a", "b", "c", "d"),
            ("h", "i", "j"),
            ("a", "c", "d"),
        ]
        threshold = 0.5
        expected_output = {
            ("a", "b", "c"): [
                (("a", "b", "d"), 0.6666666666666666),
                (("a", "b", "c", "d"), 0.6),
            ],
            ("a", "b", "d"): [(("a", "b", "c", "d"), 0.6)],
            ("a", "b", "c", "d"): [(("a", "c", "d"), 0.6)],
        }

        result = evaluate_duplicates(data, threshold)


if __name__ == "__main__":
    unittest.main()
