import argparse
import random
from array_utils import get_freqs, int_dict_as_array
from riffle_shuffle import nb_head
import matplotlib.pyplot as plt
from gauss import pdf
from math import sqrt

def coin_toss(nb_max):
    return [random.randrange(0,2) for i in range(nb_max)]

def bernoulli(nb_toss, nb_trials, probab=0.5):
    res = [0] * (nb_toss + 1)
    for i in range(nb_trials):
        res [ nb_head(nb_toss, probab) ] += 1
    return res

def count_integers(array , n):
    "Returns the count of integers [0..n-1]"
    freqs = get_freqs(array)
    freqs = dict((k, freqs.get(k,0)) for k in range(n))
    return int_dict_as_array(freqs)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate coin toss experiment')
    parser.add_argument('nb_toss', type=int, help='number of coin toss')
    parser.add_argument('nb_trials', type=int, help='number of trials')
    parser.add_argument('--probab', type=float, help='probability to get head', default=.5)
    args = parser.parse_args()
    nb_toss = args.nb_toss
    nb_trials = args.nb_trials
    probab = args.probab


    res = bernoulli(nb_toss,nb_trials, probab)
    res = [ x / nb_trials for x in res]
    plt.bar(range(len(res)),res)
    plt.plot([pdf(x, nb_toss/2, sqrt(nb_toss)/2) for x in range(nb_toss)])

    plt.show()

