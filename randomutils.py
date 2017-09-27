import random
from gauss import pdf
from math import sqrt, exp, log
from distance import euclideanDist

def oneOf(array):
    "Chooses a single random element from an array"
    return random.sample(array,1)[0]

def maxwell(sigma):
    "A random value drawn from a Maxwell-Boltzmann distribution"
    rand = (random.gauss(0,sigma), random.gauss(0,sigma), random.gauss(0,sigma)) 
    origin = (0, 0, 0)
    return euclideanDist(origin, rand)

def rayleigh_pdf(x, sigma=1):
    return  (x/sigma**2) * exp((-x**2)/(2*sigma**2))

def exponential(scale):#scale = 1/lambda
    u = random.random()
    return -log(u)/scale

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy
    plt.hist([exponential(1/5) for i in range(1000)],alpha=0.7)
    plt.hist([numpy.random.exponential(5) for i in range(1000)],alpha=0.7)
    plt.show()
