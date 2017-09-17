import random

def shuffle(array):
    n = len(array)
    for i in range(n):
        r = random.randrange(i,n)
        array[i], array[r] = array[r],array[i]
    return array

def badShuffle(array):
    n = len(array)
    for i in range(n):
        r = random.randrange(0,n)
        array[i], array[r] = array[r],array[i]
    return array
