import argparse
import math
import sys
sys.path.append('../')
import stddraw

from ioutils import read_strings
from wordcount import words
import shelve
from web_analysis import TRANS_MATR_KEY
from numpy import cumsum
from numpy.random import choice


def choose_page(probs):
    pages = list(range(len(probs)))
    return choice(pages, size=1, p=probs)[0]


if __name__ == "__main__":
    d = shelve.open('transmatrfile')
    trns_matr= d[TRANS_MATR_KEY]
    d.close()
    # print(trns_matr)

    parser = argparse.ArgumentParser(description='Simulation of page visits to calculate page rank (using Markov)')
    parser.add_argument('nb_visits', type=int, help='number of page visits allowed for the user')
    args = parser.parse_args()
    nb_visits = args.nb_visits
    # print(row)
    visiting = 0
    count_visits = [0] * len(trns_matr[0])
    for i in range(nb_visits):
        probs_row=trns_matr[visiting]
        visiting = choose_page(probs_row)
        count_visits[visiting] += 1
    count_visits = [ x / nb_visits for x in count_visits]
    print(count_visits)
    stddraw.setXscale(0,len(count_visits))
    stddraw.setYscale(0,1)
    for j, val in enumerate(count_visits):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledRectangle(j,0,1,val)
    stddraw.show()
