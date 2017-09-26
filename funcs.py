import math
def lg(n):
    return math.log(n,2)

def lg_(n):
    n_ = n
    count = 0
    while n_ >= 2:
        count += 1
        n_ //= 2
    return count

def signum(x):
    if x > 0 :
        return 1
    elif x < 0 :
        return -1
    return 0

def realBoolean2D(matr):
    res = []
    for row in matr:
        res += [[x==1 for x in row]]
    return res

def minus(array, num):
    return [ x - num for x in array ]

def multiply(array, num):
    return [ x * num for x in array ]

def scale(array):
    "Scale the array between 0 and 1"
    factor = max(array)-min(array)
    return [ (x - min(array))/factor  for x in array ]

def homothety(array, center=0, scale=1):
    return [ (x - center) * scale for x in array]

def linear_scale(array, xmin, xmax):
    array_ = scale(array)
    assert xmin < xmax
    return [ xmin + x * abs(xmax-xmin) for x in array_]



def wedge_between(array):
    min_array = min(array)
    max_array = max(array)
    array_ = minus(array, min_array)
    return scale(array_)

def any_(array):
    for b in array:
        if b:
            return True
    return False

def all_(array):
    for b in array:
        if not b:
            return False
    return True

def any__(array):
    return True in array

def all__(array):
    return False not in array

    


