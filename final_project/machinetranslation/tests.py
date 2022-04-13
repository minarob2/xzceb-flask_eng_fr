import unittest
from translator import english_to_french
from translator import french_to_english
class TestMyModule(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bienvenu'),'Welcome')
        self.assertNotEqual(french_to_english('Hello'),'Bonjour')
class TestMyModule1(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Au revoir'),'GoodBye')

unittest.main()



