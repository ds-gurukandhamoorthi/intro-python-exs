import sys
from sys import stdin

lo = float(sys.argv[1])
hi = float(sys.argv[2])

for line in stdin:
    n = float(line.strip())
    if lo <= n <= hi:
        print(n)


