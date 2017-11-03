from sys import stdin
from strutils import words

def split_line(line):
    splt = line.split(' (')
    misspelling = splt[0]
    correct = splt[1].split(')')[0]
    return misspelling, correct

def main():
    corrections = {}
    with open('../misspellings.txt') as misspellings_corrrections:
        for line in misspellings_corrrections:
            misspelling, correct = split_line(line)
            corrections[misspelling] = correct

    for line in stdin:
        for word in words(line):
            if word in corrections:
                print(corrections[word])
            else:
                print(word)

if __name__ == "__main__":
    main()
