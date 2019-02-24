import unittest
from lexer import Lexer

class LexerTest(unittest.TestCase):
    def test_grep(self):
        l = Lexer("grep")
        self.assertEqual(l.getToken(), 'KW_GREP')
        self.assertEqual(l.getLexeme(), 'grep')

    def test_ping(self):
        l = Lexer("ping")
        self.assertEqual(l.getToken(), 'KW_PING')
        self.assertEqual(l.getLexeme(), 'ping')

    def test_ls(self):
        l = Lexer("ls")
        self.assertEqual(l.getToken(), 'KW_LS')
        self.assertEqual(l.getLexeme(), 'ls')