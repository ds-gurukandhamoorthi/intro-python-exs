from math import log

def log_factorial(n):
    return sum(log(i) for i in range(1,n+1))


