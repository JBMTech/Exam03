import unittest
from src.level_2.py_mirror_matrix import mirror_matrix


class TestMirrorMatrix(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            mirror_matrix([[1, 2, 3], [4, 5, 6]]), [[3, 2, 1], [6, 5, 4]])

    def test_2(self):
        self.assertEqual(
            mirror_matrix([[1, 2], [3, 4], [5, 6]]), [[2, 1], [4, 3], [6, 5]])

    def test_3(self):
        self.assertEqual(
            mirror_matrix([[7]]), [[7]])

    def test_4(self):
        self.assertEqual(
            mirror_matrix([[1, 2, 3, 4]]), [[4, 3, 2, 1]])

    def test_5(self):
        self.assertEqual(
            mirror_matrix([[-1, -2], [-3, -4]]), [[-2, -1], [-4, -3]])


if __name__ == "__main__":
    unittest.main()
