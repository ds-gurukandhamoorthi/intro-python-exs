import argparse
import random
import sys
from numpy.random import choice



def get_coupon(n, penalise=None):
    if penalise==None:
        return random.randrange(0,n)
    probs = get_penalised_probs(n, penalise)
    return choice(range(n), size=1, p=probs)[0]

def get_penalised_probs(n, penalise):
    probs = [0] * n
    penalised_prob = n/1000
    total_penalised_prob = len(penalise) * n/1000 
    ordinary_prob = (1-total_penalised_prob) /(n-len(penalise))
    for i in range(n):
        if i in penalise:
            probs[i] = penalised_prob
        else:
            probs[i] = ordinary_prob
    return probs




def couponCollector(n):
    collected = [False]*n
    steps = 0
    while not all(collected):
        steps += 1
        samp = get_coupon(n, penalise=[0,1])
        collected[samp] = True
    return steps

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate number of coupons you need to collect before you obtain each type')
    parser.add_argument('n', type=int, help='number of distinct coupons')
    parser.add_argument('nb_trials', type=int, help='number of times the experiment must be carried on')
    args = parser.parse_args()
    n = args.n
    nb_trials = args.nb_trials


    nb_trials = int(sys.argv[2])
    totalSteps = 0
    for i in range(0,nb_trials):
        totalSteps += couponCollector(n)

    print(totalSteps/nb_trials)






