import math
import sys


def taylor_series(x, init, step):
    total = init
    prev = init
    n=1
    while True:
        # print(n, prev)
        curr = step(prev, x, n)
        if total == total + curr:
            return total
        prev = curr
        total += curr
        n+=1

def taylor_series_coeffs(init, n, step):
    res = [init]
    for i in range(1,n):
        res += [step(res[i-1],1,i)] # we choose 1 as we merely want the coefficients
    return res


def stepExp(prev,x, n):
    return  prev *x /n

def stepSinus(prev, x, n):
    # sign = 1 if n % 2 == 0 else -1
    sign = -1
    return prev *x*x/((n*2)*(n*2+1)) *sign

def stepCosinus(prev, x, n):
    sign = -1
    return prev *x*x/((n*2)*(n*2-1)) *sign

def step_phi(prev, x, n):
    return prev * x * x /(2*n + 1)

if __name__ == "__main__":
    x = float(sys.argv[1]) 

    print( taylor_series(x, x, stepSinus) )
    print( taylor_series(x, 1, stepCosinus) )
    print( taylor_series(x, 1, stepExp) )
    print( taylor_series(x, x, step_phi) )
    print( taylor_series_coeffs( 1, 5, stepExp))

