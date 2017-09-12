import sys
import math

# n = int(sys.argv[1])
n = 10

power = 1
for i in range(n+1):
    power *= 2
    print(str(math.log(power)), str(power), str(power*math.log(power)), str(power**2), str(power**3), sep='\t')
