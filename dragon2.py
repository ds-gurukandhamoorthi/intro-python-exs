import sys
import functools



@functools.lru_cache(maxsize=128)
def dragon_(n, direc='L'):
    if n == 0:
        return 'F'
    return dragon(n-1, 'L') + direc + dragon(n-1,'R')

@functools.lru_cache(maxsize=128)
def dragon(n, direc='-'):
    if n == 0:
        return 'F'
    return dragon(n-1, '-') + direc + dragon(n-1,'+')


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(dragon_(n))
    print(dragon(n))
