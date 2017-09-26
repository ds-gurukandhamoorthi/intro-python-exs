import sys
from sys import stdin
from strutils import words

def readStringArray(n, func=None):
    array = [None] * n
    i = 0
    for i in range(n):
        line = stdin.readline().strip()
        if func is None:
            array[i] = line
        else:
            array[i] = func(line)
    return array

def readIntArray(n):
    return readStringArray(n, int)

def readFloatArray(n):
    return readStringArray(n, float)

def readFloatMatrixOrVector():
    dimens=words(readStringArray(1)[0])
    dimens = [int(n) for n in dimens]
    if len(dimens) == 1:
        line = readStringArray(1)[0]
        return line_as_floats(line)

    [nb_row, nb_col] = dimens
    array = readStringArray(nb_row)
    res =[]
    for row in array:
        res += [line_as_floats(row)]
    return res

def line_as_floats(line):
    return [float(x) for x in words(line)]




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
    # n = int(sys.argv[1])
    # array = [0] * n
    # array = readFloatArray(n)

    # array = readStrings(int)

    # print(array)
    print(readFloatMatrixOrVector())
    print(readFloatMatrixOrVector())
