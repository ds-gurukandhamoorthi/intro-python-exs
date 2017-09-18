import sys
from ioutils import readFloatArray
from mathutils import std_dev

import math



if __name__ == "__main__":
    n = int(sys.argv[1])
    array = readFloatArray(n)
    print(std_dev(array))

