import unittest
from py_inter import inter


class Inter(unittest.TestCase):

    def test_1(self):
        self.assertEqual(inter("hello", "world"), "lo")

    def test_2(self):
        self.assertEqual(inter("banana", "band"), "ban")

    def test_3(self):
        self.assertEqual(inter("abcabc", "bc"), "bc")

    def test_4(self):
        self.assertEqual(inter("abc", "xyz"), "")

    def test_5(self):
        self.assertEqual(inter("", "abc"), "")


if __name__ == "__main__":
    unittest.main()
