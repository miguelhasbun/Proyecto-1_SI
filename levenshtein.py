import sys
from trie import *
import random
trie = Trie()
WORD_TARGET = sys.argv[1]

class levenshtein:
    def __init__(self):
        tam =len(word)
        c=0
        for x in range(1,tam):
            if word[x-1]!='g' or word[x-1]!='r' or word[x-1]!='e' or word[x-1]!='p' or word[x-1]!='i' or word[x-1]!='n' or word[x-1]!='l' or word[x-1]!='s':
                c=c+1
        self.max_cost = c

    def search(self, word):
        currRow = range( len( word ) + 1 )
        results = []

        for char in trie.children:
            self.levenshteinDistance( trie.children[char], char, word, currRow, results )

        return results[0]

    def levenshteinDistance(self, node, char, word, prevRow, results):
        cols = len( word ) + 1
        currRow = [prevRow[0] + 1]

        for col in range( 1, cols ):
            insertCost = currRow[col - 1] + 1
            deleteCost = prevRow[col] + 1

            if word[col - 1] != char:
                replaceCost = prevRow[ col - 1 ] + 1
            else:                
                replaceCost = prevRow[ col - 1 ]

            currRow.append( min( insertCost, deleteCost, replaceCost ) )

        if currRow[-1] <= self.max_cost and node.word != None:
            results.append( ( node.word) )

        if min( currRow ) <= self.max_cost:
            for letter in node.children:
                self.levenshteinDistance( node.children[letter], letter, word, currRow, results )

        return None

for word in WORDS:
    trie.insert(word)

l = levenshtein()

if WORD_TARGET=="grep" or WORD_TARGET=="ping" or WORD_TARGET=="ls":
    resultss=WORD_TARGET
else:
    print ("Did you meant to say:",l.search(WORD_TARGET))
    resultss = l.search(WORD_TARGET)

if len(resultss) == 0:
    print('You have not written any commands!')
else:
    if resultss == "grep":
        print('grep is a command-line utility for searching plain-text data sets for lines that match a regular expression')
    elif resultss=="ping":
        print('The ping is used to test the ability of the source computer to reach a specified destination computer. ')
    elif resultss == "ls":
        print('ls is a command to list computer files in Unix and Unix-like operating systems.')
    else:
        print('Unrecognised argument.')