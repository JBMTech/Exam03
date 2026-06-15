import unittest
from py_cryptic_sorter import cryptic_sorter


class TestCrypticSorter(unittest.TestCase):

    def test_mixed_words(self):
        self.assertEqual(
            cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]),
            ["cat", "dog", "apple", "banana", "elephant"]
        )

    def test_same_length_different_case(self):
        self.assertEqual(
            cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]),
            ["aaa", "AAA", "bbb", "BBB"]
        )

    def test_normal_words(self):
        self.assertEqual(
            cryptic_sorter(["hello", "world", "hi", "test"]),
            ["hi", "test", "hello", "world"]
        )

    def test_empty_list(self):
        self.assertEqual(
            cryptic_sorter([]),
            []
        )

    def test_single_empty_string(self):
        self.assertEqual(
            cryptic_sorter([""]),
            [""]
        )


if __name__ == "__main__":
    unittest.main()
