import sys
import random
import numpy as np
from strutils import words


def selection_sort(array):
    array = np.array(array)
    for i, e in enumerate(array):
        # elem_min, index_min = min((array[j], j) for j in range(i, len(array)))
        index_min = i + np.argmin(array[i:])
        elem_min = array[index_min]
        array[i], array[index_min] = elem_min, e
    return array


if __name__ == "__main__":
    a = [random.randrange(10) for i in range(1000)]
    print(a)
    print(selection_sort(a))
    filename = sys.argv[1]
    with open(filename) as lines:
        wordslist = [word for line in lines for word in words(line)]
    np.set_printoptions(threshold=np.nan)
    print(selection_sort(wordslist))
