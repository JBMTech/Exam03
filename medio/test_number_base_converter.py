import unittest
from py_number_base_converter import number_base_converter


class TestNumberBaseConverter(unittest.TestCase):

    def test_decimal_to_hex(self):
        self.assertEqual(
            number_base_converter("255", 10, 16),
            "FF"
        )

    def test_decimal_to_binary(self):
        self.assertEqual(
            number_base_converter("123", 10, 2),
            "1111011"
        )

    def test_base36_to_decimal(self):
        self.assertEqual(
            number_base_converter("Z", 36, 10),
            "35"
        )

    def test_decimal_to_base36(self):
        self.assertEqual(
            number_base_converter("35", 10, 36),
            "Z"
        )

    def test_invalid_base(self):
        self.assertEqual(
            number_base_converter("123", 1, 10),
            "ERROR"
        )

    def test_invalid_digit(self):
        self.assertEqual(
            number_base_converter("G", 16, 10),
            "ERROR"
        )


if __name__ == "__main__":
    unittest.main()
