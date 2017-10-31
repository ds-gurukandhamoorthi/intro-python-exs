import sys
import random
import re
from strutils import words


def quick_sort_(array):
    n = len(array)
    if n <= 1:
        return array
    left = []
    right = []
    pivot_list = []
    pivot = array[0]
    for elem in array:
        if elem < pivot:
            left += [elem]
        elif elem > pivot:
            right += [elem]
        else:
            pivot_list += [elem]
    left = quick_sort_(left)
    right = quick_sort_(right)
    return left +pivot_list + right

def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    pivot = array[0]
    # left = quick_sort([e for e in array if e < pivot])
    # right = quick_sort([e for e in array if e > pivot])
    lt, gt = lambda x: x < pivot, lambda x: x > pivot
    left = quick_sort(list(filter(lt, array)))
    right = quick_sort(list(filter(gt, array)))
    repeat = n - (len(left) + len(right))
    return left + [pivot] * repeat + right








if __name__ == "__main__":
    a = [random.randrange(10) for i in range(1000)]
    print(a)
    print(quick_sort(a))
    filename = sys.argv[1]
    with open(filename) as inp:
        lines = inp.read().split('\n')
        wordslist = [word for line in lines for word in words(line)]
    print(quick_sort_(wordslist))
