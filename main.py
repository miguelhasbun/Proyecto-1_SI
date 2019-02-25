from trie import *
from levenshtein import *

WORD_TARGET = sys.argv[1]

for word in WORDS:
    trie.insert(word)

l = levenshtein()

if WORD_TARGET=="grep" or WORD_TARGET=="ping" or WORD_TARGET=="ls":
    result = WORD_TARGET
else:
    print ("Did you meant to say:",l.search(WORD_TARGET))
    result = l.search(WORD_TARGET)

if len(result) == 0:
    print('You have not written any commands!')
else:
    if result == "grep":
        print('grep is a command-line utility for searching plain-text data sets for lines that match a regular expression')
    elif result == "ping":
        print('The ping is used to test the ability of the source computer to reach a specified destination computer. ')
    elif result == "ls":
        print('ls is a command to list computer files in Unix and Unix-like operating systems.')
    else:
        print('Unrecognised argument.')