import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(englishToFrench(''),'')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(englishToFrench(''),'')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        
unittest.main()