import unittest
from trie import *
from levenshtein import *

class Test(unittest.TestCase):
    def test_grep(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('grup')
        self.assertEqual(res, 'grep')

    def test_ping(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('pinh')
        self.assertEqual(res, 'ping')

    def test_ls(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('lss')
        self.assertEqual(res, 'ls')