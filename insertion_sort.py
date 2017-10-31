import sys
import random
from itertools import takewhile
from strutils import words


def insertion_sort_(array):
    n = len(array)
    if n == 1:
        return array
    for i in range(1, n):
        j = i
        while j > 0 and (array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def insert(sorted_array, elem):
    prefix = list(takewhile(lambda x: x <= elem, sorted_array))
    n = len(prefix)
    return prefix + [elem] + sorted_array[n:]

# def insertion_sort(array, sorted_prefix=[]):
#     if len(array) == 0:
#         return sorted_prefix
#     return insertion_sort(array[1:], insert(sorted_prefix, array[0]))


def insertion_sort(array):
    sorted_prefix = []
    while array:
        array, elem = array[1:], array[0]
        sorted_prefix = insert(sorted_prefix, elem)
    return sorted_prefix


if __name__ == "__main__":
    a = [1, 2, 3, 5, 6]
    print(insert(a, 4))
    # a=[2,1,3,5, 6]
    a = [random.randrange(10) for i in range(100)]
    assert insertion_sort(a) == sorted(a)
    filename = sys.argv[1]
    with open(filename) as inp:
        lines = inp.read().split('\n')
        wordslist = [word for line in lines for word in words(line)]
    print(insertion_sort(wordslist))
