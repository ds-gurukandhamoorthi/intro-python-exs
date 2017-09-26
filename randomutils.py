import random
from gauss import pdf
from math import sqrt, exp
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

