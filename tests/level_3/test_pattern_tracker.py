import unittest
from src.level_3.py_pattern_tracker import pattern_tracker


class TestPatternTracker(unittest.TestCase):

    def test_123(self):
        self.assertEqual(pattern_tracker("123"), 2)

    def test_12a34(self):
        self.assertEqual(pattern_tracker("12a34"), 2)

    def test_descending(self):
        self.assertEqual(pattern_tracker("987654321"), 0)

    def test_full_sequence(self):
        self.assertEqual(pattern_tracker("01234567"), 7)

    def test_letters_only(self):
        self.assertEqual(pattern_tracker("abc"), 0)

    def test_separated_digits(self):
        self.assertEqual(pattern_tracker("1a2b3c4"), 0)

    def test_repeated_digits(self):
        self.assertEqual(pattern_tracker("112233"), 2)


if __name__ == "__main__":
    unittest.main()
