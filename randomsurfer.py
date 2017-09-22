import argparse
import math
import sys
sys.path.append('../')
import stddraw
from matrixutils import matrMult

from ioutils import read_strings
from wordcount import words
import shelve
from web_analysis import TRANS_MATR_KEY
from numpy import cumsum
from numpy.random import choice


def choose_page(probs):
    pages = list(range(len(probs)))
    return choice(pages, size=1, p=probs)[0]

def hitting_time(probs, startpage):
    count = 0
    while True:
        count += 1
        go_page = choice(range(len(probs)), size=1, p=probs)[0]
        if go_page == startpage:
            return count

def avg_hitting_time(probs,startpage, nb_trials):
    total = 0
    for i in range(nb_trials):
        total += hitting_time(probs, startpage)
    return total / nb_trials

def coverage_time(probs, startpage):
    covered = [False] * len(probs)
    count = 0
    while True:
        count += 1
        go_page = choice(range(len(probs)), size=1, p=probs)[0]
        covered[go_page] = True
        if all(covered):
            return count

def avg_coverage_time(probs,startpage, nb_trials):
    total = 0
    for i in range(nb_trials):
        total += coverage_time(probs, startpage)
    return total / nb_trials





if __name__ == "__main__":
    d = shelve.open('transmatrfile')
    trns_matr= d[TRANS_MATR_KEY]
    d.close()
    # print(trns_matr)

    parser = argparse.ArgumentParser(description='Simulation of page visits to calculate page rank (using Markov)')
    parser.add_argument('nb_visits', type=int, help='number of page visits allowed for the user')
    parser.add_argument('--histogram', help='show histogram', action='store_true')
    parser.add_argument('--analyse-hitting-time', type=int, help='number of trials for analysing hitting time')
    parser.add_argument('--analyse-coverage-time', type=int, help='number of trials for analysing coverage time')
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

    ranks_vector=[0]*len(trns_matr[0])
    ranks_vector[0]=1
    ranks_vector=[ranks_vector]
    res = matrMult(ranks_vector, trns_matr)
    print("res", res)
    for i in range(20):
        res = matrMult(res, trns_matr)
        print("res", res)

    print('***')
    rank_and_page = [(val,i) for i, val in enumerate(res[0])]
    print(rank_and_page)
    print('***')
    print(sorted(rank_and_page, reverse=True))

    
    # res = trns_matr
    # for i in range(20):
    #     res = matrMult(res, trns_matr)
    # print(res)

    # res = trns_matr
    # for i in range(4):
    #     res = matrMult(res, res)
    # print(res)

    if args.histogram:
        stddraw.setXscale(0,len(count_visits))
        stddraw.setYscale(0,1)
        for j, val in enumerate(count_visits):
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(j,0,1,val)
        stddraw.show()
    if args.analyse_hitting_time:
        NB_TRIALS = args.analyse_hitting_time
        #Hitting time
        stat_hitting_time=[0]*len(trns_matr)
        for i, probs in enumerate(trns_matr):
            stat_hitting_time[i] = avg_hitting_time(probs, i, NB_TRIALS)
        print(stat_hitting_time)
    if args.analyse_coverage_time:
        NB_TRIALS = args.analyse_coverage_time
        #Coverage time
        stat_coverage_time=[0]*len(trns_matr)
        for i, probs in enumerate(trns_matr):
            stat_coverage_time[i] = avg_coverage_time(probs, i, NB_TRIALS)
        print(stat_coverage_time)


