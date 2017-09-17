import sys
import printBoolArray




def relativelyPrimeSieve(n):
    sieve = [[True]*n for i in range(n)]
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            # sieve[i-1][j-1] = False
            # sieve[j-1][i-1] = False
            for k in range(i,n+1,i):
                sieve[j-1][k-1] = False
                sieve[k-1][j-1] = False
    return sieve


if __name__ == "__main__":
    n = int(sys.argv[1])
    sieve = relativelyPrimeSieve(n)
    printBoolArray.printMatrix(sieve)
