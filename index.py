import sys
from collections import defaultdict
from strutils import words
from BST import BinarySearchTree
# from bintrees import FastAVLTree


def index_of_words_(filename):
    index = BinarySearchTree()
    with open(filename) as inp:
        i = 0
        for line in inp:
            for word in words(line):
                i += 1
                if word in index:
                    index[word] = index[word] + [i]
                else:
                    index[word] = [i]
    return index

def index_of_words(filename):
    index = defaultdict(list)
    with open(filename) as inp:
        i = 0
        for line in inp:
            for word in words(line):
                i += 1
                index[word] += [i]
    return index


def main():
    filename = sys.argv[1]
    index = index_of_words(filename)
    for word in index:
        print(word, index[word])


if __name__ == "__main__":
    main()
