import math
import sys

n = int(sys.argv[1])

def sieveEratoshenes(n):
    "calculate the sieve of Eratoshtenes for primatlity"
    sieve = [True] * (n+1)
    sieve[1] = False
    maxiter =  int(math.sqrt(n))
    for i in range(2, maxiter+1, 1):
        for j in range(i*2, n+1, i):
            sieve[j] = False
    return sieve[1:]

def nbPrimes(n):
    sieve = sieveEratoshenes(n)
    return sieve.count(True)

# print(sieveEratoshenes(n))
print(nbPrimes(n))

        

