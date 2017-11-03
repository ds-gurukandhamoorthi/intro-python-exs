import sys
from collections import defaultdict
from strutils import words
from BST import BinarySearchTree
# from bintrees import FastAVLTree

def split_index(line):
    splt = line.split(' [')
    word = splt[0]
    rest = splt[1].split(']')[0]
    indexes = [int(i) for i in rest.split(', ')]
    return word, indexes



def inverse_index(filename, nb_words):
    inverted_index = [''] * nb_words 
    with open(filename) as inp:
        for line in inp:
            word, indexes = split_index(line)
            for i in indexes:
                if i < nb_words + 1:
                    inverted_index[i-1] = word
    return inverted_index


def main():
    filename = sys.argv[1]
    invrtd_idx = inverse_index(filename, 100)
    for word in invrtd_idx:
        print(word, end= ' ')


if __name__ == "__main__":
    main()
