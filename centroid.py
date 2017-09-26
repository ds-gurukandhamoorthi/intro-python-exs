from ioutils import read_strings
from strutils import words

array = read_strings()
mtot  = 0 
mxtot = 0
mytot = 0
for line in array:
    [m, x, y] = words(line)[0:3]
    m, x, y = float(m), float(x), float(y)
    mtot += m
    mxtot += (m * x)
    mytot += (m * y)

print(mxtot/mtot , mytot/mtot)


