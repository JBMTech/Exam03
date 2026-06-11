import unittest
from py_twist_sequence import twist_sequence


class TestTwistSequence(unittest.TestCase):

    def test_rotate_by_two(self):
        self.assertEqual(
            twist_sequence([1, 2, 3, 4, 5], 2),
            [4, 5, 1, 2, 3]
        )

    def test_rotate_by_one(self):
        self.assertEqual(
            twist_sequence([1, 2, 3], 1),
            [3, 1, 2]
        )

    def test_rotate_by_zero(self):
        self.assertEqual(
            twist_sequence([1, 2, 3, 4], 0),
            [1, 2, 3, 4]
        )

    def test_rotate_more_than_length(self):
        self.assertEqual(
            twist_sequence([1, 2, 3], 5),
            [2, 3, 1]
        )

    def test_empty_list(self):
        self.assertEqual(
            twist_sequence([], 3),
            []
        )


if __name__ == "__main__":
    unittest.main()
