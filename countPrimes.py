import sys
import math

n = int(sys.argv[1])



def findOneStrictFactor(n):
    if n % 2 == 0:
        return True
    for i in range(3, int(math.sqrt(n))+1, 2):
        if (n % i) == 0:
            return True
    return False

def countPrimes(n):
    nbPrimes = 1 if n >= 2 else 0
    for i in range(3,n,2):
        if not findOneStrictFactor(i):
            nbPrimes += 1
    return nbPrimes

print(countPrimes(n))
