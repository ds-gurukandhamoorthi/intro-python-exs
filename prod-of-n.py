import sys
import math
n = int(sys.argv[1])
prod = 1

for i in range(1, n+1):
    prod *= i
print(prod)

print(math.factorial(n))

