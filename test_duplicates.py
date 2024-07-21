import unittest
from duplicates import rate_similarity, evaluate_duplicates

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
