import sys
from Interval import Interval
from ioutils import read_strings

if __name__ == "__main__":
    x = float(sys.argv[1])
    strs = read_strings()
    for s in strs:
        flts = [float(x) for x in s.split()]
        intrvl = Interval(flts[0], flts[1])
        if x in intrvl:
            print(intrvl)

        

