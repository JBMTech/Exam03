import unittest
from src.level_4.py_anagram import anagram


class Anagram(unittest.TestCase):

    def test_1(self):
        self.assertTrue(anagram("listen", "silent"))

    def test_2(self):
        self.assertTrue(anagram("Triangle", "Integral"))

    def test_3(self):
        self.assertTrue(anagram("Dormitory", "Dirty Room"))

    def test_4(self):
        self.assertFalse(anagram("hello", "world"))

    def test_5(self):
        self.assertTrue(anagram("", ""))

    def test_6(self):
        self.assertFalse(anagram("abc", "abcc"))


if __name__ == "__main__":
    unittest.main()
