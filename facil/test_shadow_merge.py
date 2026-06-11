import unittest
from py_shadow_merge import shadow_merge


class ShadowMerge(unittest.TestCase):

    def test_1(self):
        self.assertEqual(shadow_merge([1, 3, 5], [2, 4, 6]),
                         [1, 2, 3, 4, 5, 6])

    def test_2(self):
        self.assertEqual(shadow_merge([1, 2, 3], [4, 5, 6]),
                         [1, 2, 3, 4, 5, 6])

    def test_3(self):
        self.assertEqual(shadow_merge([1], [2, 3, 4]),
                         [1, 2, 3, 4])

    def test_4(self):
        self.assertEqual(shadow_merge([], [1, 2, 3]),
                         [1, 2, 3])

    def test_5(self):
        self.assertEqual(shadow_merge([1, 1, 2], [1, 3, 3]),
                         [1, 1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
