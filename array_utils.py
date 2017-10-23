import random
from mathutils import avg


def shuffle(array):
    n = len(array)
    for i in range(n):
        r = random.randrange(i,n)
        array[i], array[r] = array[r],array[i]
    return array

def bad_shuffle(array):
    n = len(array)
    for i in range(n):
        r = random.randrange(0,n)
        array[i], array[r] = array[r],array[i]
    return array

def normalize(array):
    "Make the array's total = 1"
    total = sum(array)
    return [x / total for x in array]


#tuple(from, to)
def group2(lst):
    return zip(lst[0::2], lst[1::2])

def group3(lst):
    return zip(lst[0::3], lst[1::3],lst[2::3])

def split_every(n, array):
    return [array[i:i+n] for i in range(0,len(array),n)]
#The difference between split_every and group2 is when len(array) is not a multiple of n

#Ramda-js inspired
def aperture(lst, k):
    return (lst[i:i+k] for  i in range(len(lst) - (k-1)))

def moving_avg(lst, k):
    res = [None] * (k-1)
    ma = []
    for array in aperture(lst, k):
        ma += [avg(array)]
    return res + ma

def int_dict_as_array(dctnry):
    mx = max(dctnry.keys())
    array = [0] * (mx + 1)
    for i, val in dctnry.items():
        array[i] = val
    return array


if __name__ == "__main__":
    print(split_every(2,[1,2,3,4,5]))
    print(list(group2([1,2,3,4,5])))
