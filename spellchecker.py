from sys import stdin
from strutils import words

def build_lexicon(filename):
    lexicon = set()
    with open(filename) as correct_words:
        for word in correct_words:
            lexicon.add(word.strip())
    return lexicon


def main():
    lexicon = build_lexicon('../words.utf-8.txt')
    for line in stdin:
        for word in words(line):
            if word not in lexicon:
                print(word)

if __name__ == "__main__":
    main()
