import unittest
from py_bracket_validator import bracket_validator


class TestBracketValidator(unittest.TestCase):

    def test_simple_parentheses(self):
        self.assertTrue(bracket_validator("()"))

    def test_multiple_types(self):
        self.assertTrue(bracket_validator("()[]{}"))

    def test_invalid_mismatch(self):
        self.assertFalse(bracket_validator("(]"))

    def test_wrong_order(self):
        self.assertFalse(bracket_validator("([)]"))

    def test_nested_correct(self):
        self.assertTrue(bracket_validator("{[]}"))

    def test_double_nested(self):
        self.assertTrue(bracket_validator("((()))"))

    def test_missing_closing(self):
        self.assertFalse(bracket_validator("((())"))

    def test_empty_string(self):
        self.assertTrue(bracket_validator(""))


if __name__ == "__main__":
    unittest.main()