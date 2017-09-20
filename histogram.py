import sys
import math
sys.path.append('../')
import stddraw
import random

from sys import stdin
from ioutils import read_floats


def indexOfFloatInterval(lo, hi, n, val):
    "Tells where val falls in the interval [lo, hi] subdivided by n"
    if not lo <= val <= hi:
        return -1
    if lo == val: 
        return 0
    if hi == val:
        return n-1
    delta = (hi - lo)/n
    val_ = val - lo
    return math.floor(val_/delta)

def histogram(array, lo, hi, n):
    hist = [0] * n
    for val in array:
        index = indexOfFloatInterval(lo, hi, n, val)
        if index >= 0:
            hist[index] += 1
    return hist




if __name__ == "__main__":
    lo = float(sys.argv[1])
    hi = float(sys.argv[2])
    n = int(sys.argv[3])
    stddraw.setXscale(0, n)
    stddraw.setYscale(0, n+1)

    array = read_floats()
    hist = histogram(array, lo, hi, n)
    print(hist)
    for i, val in enumerate(hist):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledRectangle(i,0,1,val)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.rectangle(i,0,1,val)
    stddraw.show()
