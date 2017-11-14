import argparse
import random
from numpy.random import choice
from binomial_distribution import binomial_dist


def get_coupon(n, penalise=None, binomial=False):
    if binomial is True:
        probs = [binomial_dist(n - 1, k, 0.5) for k in range(0, n)]
        assert len(probs) == n
        return choice(range(n), size=1, p=probs)[0]
    if penalise is None:
        return random.randrange(0, n)
    probs = get_penalised_probs(n, penalise)
    return choice(range(n), size=1, p=probs)[0]


def get_penalised_probs(n, penalise):
    probs = [0] * n
    penalised_prob = n / 1000
    total_penalised_prob = len(penalise) * n / 1000
    ordinary_prob = (1 - total_penalised_prob) / (n - len(penalise))
    for i in range(n):
        if i in penalise:
            probs[i] = penalised_prob
        else:
            probs[i] = ordinary_prob
    return probs


def couponCollector(n, penalise=None, binomial=False):
    collected = [False] * n
    steps = 0
    while not all(collected):
        steps += 1
        if binomial is True:
            samp = get_coupon(n, penalise=None, binomial=True)
        elif penalise is None:
            samp = get_coupon(n, penalise=None, binomial=False)
        else:
            samp = get_coupon(n, penalise, binomial=False)
        collected[samp] = True
    return steps


def main():
    parser = argparse.ArgumentParser(
        description='Estimate number of coupons you need to collect before you obtain each type')
    parser.add_argument('n', type=int, help='number of distinct coupons')
    parser.add_argument('nb_trials', type=int,
                        help='number of times the experiment must be carried on')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--penalise', metavar='N', type=int,
                       nargs='+', help='coupon numbers to penalise ')
    group.add_argument('--binomial', help='help for ', action='store_true')

    args = parser.parse_args()
    n = args.n
    nb_trials = args.nb_trials
    penalise = args.penalise
    binomial = args.binomial

    totalSteps = 0
    for i in range(nb_trials):
        totalSteps += couponCollector(n, penalise, binomial)

    print(totalSteps / nb_trials)
if __name__ == "__main__":
    main()
