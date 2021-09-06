import unittest

from translator import english_french, french_english

class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_french('Hello'), 'Bonjour')

    def test_fr_to_en(self):
        self.assertEqual(french_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()