import sys
import functools

n = int(sys.argv[1])


@functools.lru_cache(maxsize=128)
def dragon(n, direc='L'):
    if n == 0:
        return 'F'
    return dragon(n-1, 'L') + direc + dragon(n-1,'R')

print(dragon(n))
