import unittest
from py_string_sculptor import string_sculptor


class TestStringSculptor(unittest.TestCase):

    def test_simple_word(self):
        self.assertEqual(string_sculptor("hello"), "hElLo")

    def test_upper_input(self):
        self.assertEqual(string_sculptor("Hello World"), "hElLo WoRlD")

    def test_with_numbers(self):
        self.assertEqual(string_sculptor("aBc123def"), "aBc123DeF")

    def test_with_symbols(self):
        self.assertEqual(string_sculptor("Python3.9!"), "pYtHoN3.9!")

    def test_empty_string(self):
        self.assertEqual(string_sculptor(""), "")


if __name__ == "__main__":
    unittest.main()
