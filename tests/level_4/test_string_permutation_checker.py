import unittest
from src.level_4.py_string_permutation_checker import (
    string_permutation_checker)


class TestStringPermutationChecker(unittest.TestCase):

    def test_simple_permutation(self):
        self.assertTrue(
            string_permutation_checker("listen", "silent")
        )

    def test_not_permutation(self):
        self.assertFalse(
            string_permutation_checker("hello", "bello")
        )

    def test_both_empty(self):
        self.assertTrue(
            string_permutation_checker("", "")
        )

    def test_one_empty(self):
        self.assertFalse(
            string_permutation_checker("a", "")
        )

    def test_case_sensitive(self):
        self.assertFalse(
            string_permutation_checker("Abc", "abc")
        )

    def test_with_spaces(self):
        self.assertTrue(
            string_permutation_checker("a gentleman", "elegant man")
        )


if __name__ == "__main__":
    unittest.main()
