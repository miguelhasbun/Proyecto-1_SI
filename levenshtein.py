import sys
from trie import *

trie = Trie()
WORD_TARGET = sys.argv[1]

class levenshtein:
    def __init__(self):
        self.max_cost = 1 #El costo es cuantas letras de diferencia hay entre la WORD_TARGET i la word en WORDS
                          #En el constructor se deberia calcular el max_cost

    def search(self, word):
        currRow = range( len( word ) + 1 )
        results = []

        for char in trie.children:
            self.levenshteinDistance( trie.children[char], char, word, currRow, results )

        return results

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
            results.append( ( node.word, currRow[-1] ) )

        if min( currRow ) <= self.max_cost:
            for letter in node.children:
                self.levenshteinDistance( node.children[letter], letter, word, currRow, results )

        return None

for word in WORDS:
    trie.insert(word)

l = levenshtein()
print (l.search(WORD_TARGET))