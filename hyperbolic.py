from math import exp

def cosh(x):
    return (exp(x) + exp(-x))/2

def sinh(x):
    return (exp(x) - exp(-x))/2

def tanh(x):
    return sinh(x)/cosh(x)

def coth(x):
    return 1/tanh(x)

def sech(x):
    return 1/cosh(x)

def csch(x):
    return 1/sinh(x)
