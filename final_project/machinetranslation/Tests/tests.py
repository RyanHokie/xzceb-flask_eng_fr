import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_eng_fr(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test output of "Bonjour" with input of "Hello"
        self.assertNotEqual(english_to_french("None"), '') #Tests null input
 
class TestfrenchToEnglish(unittest.TestCase): 
    def test_fr_eng(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello' ) # test output of "Hello" with input of "Bonjour"
        self.assertNotEqual(french_to_english("None"), '') #Tests null input


unittest.main()