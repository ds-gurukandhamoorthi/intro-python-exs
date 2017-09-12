import math
import sys
x = float(sys.argv[1]) 



# def fact(n):
#     res = 1
#     for i in range(2,n+1):
#         res *= i
#     return res

# def termExp(x,n):
#     if(n==1):
#         return 1
#     return (x**n)/fact(n)


# def exponential(x,n):
#     total = 1.0
#     for i in range(1,n+1):
#         total += termExp(x,i)
#     return total
# print(exponential(x,n))

def taylorSeries(x, init, step):
    total = init
    prev = init
    n=1
    while True:
        print(n, prev)
        curr = step(prev, x, n)
        if total == total + curr:
            return total
        prev = curr
        total += curr
        n+=1

def stepExp(prev,x, n):
    return  prev *x /n

def stepSinus(prev, x, n):
    # sign = 1 if n % 2 == 0 else -1
    sign = -1
    return prev *x*x/((n*2)*(n*2+1)) *sign

def stepCosinus(prev, x, n):
    sign = -1
    return prev *x*x/((n*2)*(n*2-1)) *sign


# print( taylorSeries(x, 1, stepExp) )
print( taylorSeries(x, x, stepSinus) )
print( taylorSeries(x, 1, stepCosinus) )

