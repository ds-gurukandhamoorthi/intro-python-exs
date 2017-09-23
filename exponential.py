import math
import sys



def fact(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res

def termExp(x,n):
    if(n==1):
        return 1
    return (x**n)/fact(n)

def exponential(x,n):
    total = 1.0
    for i in range(1,n+1):
        total += termExp(x,i)
    return total

#SEE taylor_series.py : There's a better implementation there
x = 1
n = 5
print(exponential(x,n))
