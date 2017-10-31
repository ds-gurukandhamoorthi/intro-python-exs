from int_utils import odd
from collections import Counter
def median(array):
    array = sorted(array)
    n = len(array)
    m = n//2
    if odd(n):
        return array[m]
    return (array[m-1] + array[m])/2

def mode(array):
    return Counter(array).most_common(1)[0][0]
