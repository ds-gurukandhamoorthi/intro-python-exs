import random
import sys

m = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(n):
    print(random.randrange(0,m))
