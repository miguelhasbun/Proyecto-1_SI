WORDS = {'grep', 'ping', 'ls'}

class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]
        node.word = word

    def find(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node = node.children[char]
            else:
                return None
        return node.word
        
#results = search( WORD_TARGET ) #results is a tuple ( word, cost )
#for res in results: print( res )
