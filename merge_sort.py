import sys
import random
from strutils import words


def merge(array1, array2):
    n = len(array1)
    m = len(array2)
    res = [None] * (n + m)
    i1 = 0
    i2 = 0
    for i, _ in enumerate(res):
        if i1 >= n:
            res[i:] = array2[i2:]
            return res
        if i2 >= m:
            res[i:] = array1[i1:]
            return res
        if array1[i1] <= array2[i2]:
            res[i] = array1[i1]
            i1 += 1
        else:
            res[i] = array2[i2]
            i2 += 1
    return res


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    m = n // 2
    left = merge_sort(array[:m])
    right = merge_sort(array[m:])
    return merge(left, right)


if __name__ == "__main__":
    a = [1, 2, 5]
    b = []
    c = [2, 4, 6]
    d = [7, 8]
    print(merge(a, b), merge(d, a))
    a = [random.randrange(10) for i in range(100)]
    print(merge_sort(a))
    filename = sys.argv[1]
    with open(filename) as lines:
        wordslist = [word for line in lines for word in words(line)]
    print(merge_sort(wordslist))
