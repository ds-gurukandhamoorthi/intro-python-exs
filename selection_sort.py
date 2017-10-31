import sys
import random
from strutils import words


def selection_sort(array):
    for i, e in enumerate(array):
        elem_min, index_min = min((array[j], j) for j in range(i, len(array)))
        array[i], array[index_min] = elem_min, e
    return array







if __name__ == "__main__":
    a = [random.randrange(10) for i in range(1000)]
    print(a)
    print(selection_sort(a))
    filename = sys.argv[1]
    with open(filename) as inp:
        lines = inp.read().split('\n')
        wordslist = [word for line in lines for word in words(line)]
    print(selection_sort(wordslist))
