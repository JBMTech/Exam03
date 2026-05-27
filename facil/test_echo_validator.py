import unittest
from py_echo_validator import echo_validator

class EchoValidator(unittest.TestCase):

    def test_1(self):
        self.assertTrue(echo_validator("A man a plan a canal Panama"))
    
    def test_2(self):
        self.assertTrue(echo_validator("Was it a car or a cat I saw"))

    def test_3(self):
        self.assertFalse(echo_validator("hello"))

    def test_4(self):
        self.assertTrue(echo_validator("Madam Im Adam"))

    def test_5(self):
        self.assertTrue(echo_validator("racecar"))

    def test_6(self):
        self.assertFalse(echo_validator(""))

if __name__ == "__main__":
    unittest.main()