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