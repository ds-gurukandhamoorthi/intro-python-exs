import random
from binomial_coefficients import binomial_coefficients
import numpy
from numpy.random import choice
import bisect
from numpy.random import binomial




def nb_head(nb_max):
    "To get binomial distribution"
    total = 0
    for i in range(nb_max-1): #nb coin toss = nb_max  -1 
        total += random.randrange(0,2)
    return total

def cumulateSum(array):
    if len(array) == 0:
        return []
    res = [array[0]]
    for i in range(1,len(array)):
       res += [res[i-1] + array[i]]
    return res


def nb_head2(nb_max):
    # probCum = cumulateSum(binomial_coefficients(nb_max))
    probCum = numpy.cumsum(binomial_coefficients(nb_max))
    prob = random.random()
    return bisect.bisect(probCum, prob)
    # for i,cumProb in enumerate(probCum):
    #     if cumProb >= prob:
    #         return i 

def nb_head3(nb_max):
    nums = list(range(nb_max))
    weighted_probs = binomial_coefficients(nb_max)
    return choice(nums, size=1, p=weighted_probs)[0] # return one elements from nums with the weighted probability

def nb_head4(nb_max):
    COIN_FLIP_PROB = .5
    return binomial(nb_max, COIN_FLIP_PROB)






NB_CARDS = 52
def riffle_shuffle(array):
    n = len(array)
    r = nb_head(n)
    left,right = array[0:r], array[r:]
    shuffled = [0] * n

    i = n - 1
    while True:
        n1 = len(left)
        n2 = len(right)
        if i >= 0 and random.random() < n1/(n1+n2):
            shuffled[i] = left[0]
            left = left[1:]
            i -= 1
        if i >= 0 and random.random() < n2/(n1+n2):
            shuffled[i] = right[0]
            right = right[1:]
            i -= 1
        if i < 0:
            return shuffled




if __name__ == "__main__":
    # print(nb_head(5))
    print(riffle_shuffle(list(range(5))))

    NB_CARDS = 52
    dist = [0] * NB_CARDS
    

    for i in range(5000):
        dist[nb_head(NB_CARDS)] += 1
    print(dist)

    dist2 = [0] * NB_CARDS
    for i in range(5000):
        dist2[nb_head2(NB_CARDS)] += 1
    print(dist2)

    dist3 = [0] * NB_CARDS
    for i in range(5000):
        dist3[nb_head2(NB_CARDS)] += 1
    print(dist3)

    dist4 = [0] * NB_CARDS
    for i in range(5000):
        dist4[nb_head2(NB_CARDS)] += 1
    print(dist4)

        


