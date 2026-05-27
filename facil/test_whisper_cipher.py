import unittest
from py_whisper_cipher import whisper_cipher

class WhisperCipher(unittest.TestCase):

    def test_1(self):
        self.assertEqual(whisper_cipher("hello", 3),"khoor")
    
    def test_2(self):
        self.assertEqual(whisper_cipher("Hello World!", 1),"Ifmmp Xpsme!")

    def test_3(self):
        self.assertEqual(whisper_cipher("xyz", 3), "abc")

    def test_4(self):
        self.assertEqual(whisper_cipher("ABC123def", 5), "FGH123ijk")

    def test_5(self):
        self.assertEqual(whisper_cipher("", 10), "")

if __name__ == "__main__":
    unittest.main()