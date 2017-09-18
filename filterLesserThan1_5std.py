import sys
from ioutils import readFloatArray
from mathutils import std_dev, avg

import math

def fartherThan(array, nb_std):
    "filters values that are lesser than given times std"
    res = []
    std = std_dev(array)
    avge = avg(array)
    for val in array:
        if not(avge -(std *nb_std) <= val <= avge +(std *nb_std)):
            res += [val]
    return res
    


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = readFloatArray(n)
    print(std_dev(array))
    print(fartherThan(array, 1.5))

