import sys
from sys import stdin

def readStringArray(n, func=None):
    array = [None] * n
    i = 0
    for i in range(n):
        line = stdin.readline()
        if func is None:
            array[i] = line.strip()
        else:
            array[i] = func(line.strip())
    return array

def readIntArray(n):
    return readStringArray(n, int)

def readFloatArray(n):
    return readStringArray(n, float)

def read_strings(func=None):
    array = []
    for line in stdin:
        line = line.strip()
        if line == '':
            return array
        if func is None:
            array += [line]
        else:
            array += [func(line)]

    return array

def read_ints():
    return read_strings(int)

def read_floats():
    return read_strings(float)

if __name__ == "__main__":
    n = int(sys.argv[1])
    array = [0] * n
    array = readFloatArray(n)

    array = readStrings(int)

    print(array)
