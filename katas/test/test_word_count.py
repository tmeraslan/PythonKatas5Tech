import unittest

from katas.word_count import count_words

class TestCountWords(unittest.TestCase):
    
    def test_regular_sentence(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_one_word(self):
        self.assertEqual(count_words("Hello"), 1)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("   Hello   world   "), 2)

    def test_tabs_and_newlines(self):
        self.assertEqual(count_words("line1\nline2\tline3"), 3)