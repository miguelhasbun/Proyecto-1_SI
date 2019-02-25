import unittest
from trie import *
from levenshtein import *

class commands:
    def test_grep(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('grup')
        self.assertEqual(res[0][0], 'grep')

    def test_ping(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('pinh')
        self.assertEqual(res[0][0], 'ping')

    def test_ls(self):
        for word in WORDS:
            trie.insert(word)
        l = Levenshtein()
        res = l.search('lss')
        self.assertEqual(res[0][0], 'ls')