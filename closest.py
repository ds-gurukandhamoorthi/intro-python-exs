import sys
from distance import squared_distance
from ioutils import read_strings
from strutils import words

if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    array = read_strings()
    res = []
    def closest(x,y,z, v1, v2):
        if squared_distance([x,y,z], v1) < squared_distance([x,y,z], v2):
            return v1
        return v2
    for line in array:
        [xi, yi, zi ] = words(line)[0:3]
        [xi, yi , zi] = [float(xi), float(yi), float(zi)]
        if res == []:
            res = [xi, yi, zi]
        else:
            res = closest(x,y,z, res, [xi, yi, xi])

    print(res)







