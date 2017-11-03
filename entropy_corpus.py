import sys
import re
from strutils import words
from array_utils import shannon_entropy_list

filename = sys.argv[1]

with open(filename) as corpus:
    wordlist = []
    for line in corpus:
        for word in words(line):
            word = word.lower()
            word = re.sub(r'[^a-z]', '', word)
            wordlist += [word]
    print(shannon_entropy_list(wordlist))
