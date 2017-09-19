from ioutils import read_floats
from mathutils import avg_magnitude, avg
from rle import rle

def avg_square(array):
    return avg([ x * x for x in array ])

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0

def zero_crossing(array):
    signs = map(sign, array)
    rles = rle(signs)
    runs_only = []
    for tup in rles:
        if tup[1] !=0:
            runs_only += [tup[1]]
    count_zc = 0
    for i in range(len(runs_only)-1):
        if runs_only[i] < 0 and runs_only[i+1] > 0:
            count_zc += 1
    return count_zc




array = read_floats()
print(avg_magnitude(array))
print(avg_square(array))
print(zero_crossing(array))
