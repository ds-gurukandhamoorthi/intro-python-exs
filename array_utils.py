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

def multiply_and_add(array1, array2):
    return sum((a * b for a, b in zip(array1, array2)))

#tuple(from, to)
def group2(lst):
    return zip(lst[0::2], lst[1::2])

def split_every(n, array):
    return [array[i:i+n] for i in range(0,len(array),n)]
#The difference between split_every and group2 is when len(array) is not a multiple of n

def get_freqs( array):
    freqs = {}
    for val in array:
        freqs[val] = freqs.get(val, 0) + 1
    return freqs

def int_dict_as_array(dctnry):
    mx = max(dctnry.keys())
    array = [0] * (mx + 1)
    for i, val in dctnry.items():
        array[i] = val
    return array


if __name__ == "__main__":
    print(split_every(2,[1,2,3,4,5]))
    print(list(group2([1,2,3,4,5])))
