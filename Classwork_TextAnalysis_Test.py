from Classwork_TextAnalysis import *
import unittest

class TestSequenceFunctions(unittest.TestCase):

  def setUp(self):
    self.text_file = open("Classwork_OriginalText.txt", "r")


  def test_imports_text(self):
    self.test_text_file = open("Classwork_OriginalText.txt", "r")
    self.test_text = self.test_text_file.read()
    self.assertEqual(import_text(self.text_file), self.test_text)

  def test_split_text(self):
    text = import_text(self.text_file)
    self.assertEqual(split_text(text), ["Frank and beans.", "Foo bar.", ""])

  def test_split_para(self):
    self.assertEqual(split_para("Frank and beans? Foo and bar!"), ["Frank and beans", "Foo and bar", ""])

  def test_split_sentence(self):
    self.assertEqual(split_sentence("Frank and beans"), ["Frank", "and", "beans"])

  

  def tearDown(self):
    self.text_file.close()

if __name__ == '__main__':
    unittest.main()
