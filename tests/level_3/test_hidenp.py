import unittest
from level_3.py_hidenp import hidenp


class Hidenp(unittest.TestCase):

    def test_1(self):
        self.assertTrue(hidenp("abc", "a1b2c3"))

    def test_2(self):
        self.assertTrue(hidenp("ace", "abcde"))

    def test_3(self):
        self.assertFalse(hidenp("aec", "abcde"))

    def test_4(self):
        self.assertTrue(hidenp("", "abc"))

    def test_5(self):
        self.assertFalse(hidenp("abc", "ab"))

    def test_6(self):
        self.assertFalse(hidenp("aaaa", "aaa"))

    def test_7(self):
        self.assertTrue(hidenp("sing", "subsequence testing"))


if __name__ == "__main__":
    unittest.main()
