import sys
import random
import re
def insertion_sort(array):
    n = len(array)
    if n == 1:
        return array
    for i in range(1, n):
        j = i
        while j > 0 and (array[j] < array[j-1]):
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


if __name__ == "__main__":
    # a=[2,1,3,5, 6]
    # a = [random.randrange(10) for i in range(100)]
    # print(insertion_sort(a))
    filename = sys.argv[1]
    with open(filename) as inp:
        lines=inp.read().split('\n')
        words = [word  for line in lines for word in re.split('\s+', line) if word != '']
    print(insertion_sort(words))
    


