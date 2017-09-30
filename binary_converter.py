import sys
import math

def symbol_for(n):
    if 10 <= n <= 15:
        return 'ABCDEF'[n-10]
    return str(n)


def change_base(n, base):
    res = ''
    if n == 0: 
        maxpower = 0
    else:
        maxpower = int(math.log(n,base))
    for i in range(maxpower, -1, -1):
        divd = n//base**i
        res += symbol_for(divd)
        n -= (base**i )*divd
    return res

def change_base_rec(n, base, res=''):
    if base<= 0 or n <=0:
        return res
    remainder = symbol_for(n%base)
    return change_base_rec(n//base, base, remainder + res)


n = int(sys.argv[1])
base = int(sys.argv[2])

print(change_base(n, base))
print(change_base_rec(n,base))
