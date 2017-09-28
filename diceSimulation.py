import random
import distance
import sys
from numpy.random import choice

def die(prob_dist=None):
    if prob_dist is None:
        return random.randrange(1,7)
    return choice(range(1,7), size=1, p=prob_dist)[0]

def simulateSumDices(nbTrials):
    freqSum = [0]*13
    for i in range(nbTrials):
        freqSum[die()+die()]+=1
    return [freq/nbTrials for freq in freqSum]

if __name__ == "__main__":
    probabilities = [0]*13

    for i in range(1, 7):
        for j in range(1, 7):
            probabilities[i+j] += 1.0

    for k in range(2, 13):
        probabilities[k] /= 36.0

    print(probabilities)

    nbTrials = int(sys.argv[1])
    res = simulateSumDices(nbTrials)
    print(res)

    expected  = probabilities

    print(distance.euclideanDist(expected,res))
    print(distance.chebyschevDist(expected,res))
    print(distance.chebyschevDist(expected,res)<0.0005)
