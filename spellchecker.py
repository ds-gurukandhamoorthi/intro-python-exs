from sys import stdin
from strutils import words
def main():
    lexicon = set()
    with open('../words.utf-8.txt') as correct_words:
        for word in correct_words:
            lexicon.add(word.strip())

    for line in stdin:
        for word in words(line):
            if word not in lexicon:
                print(word)

if __name__ == "__main__":
    main()
