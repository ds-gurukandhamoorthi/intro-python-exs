from matrixutils import rand_bool_matr
from pprint import pprint
import matplotlib.pyplot as plt
import argparse
from matrixutils import transpose, dimen, rand_bool_matrix_3d
from geomutils import neighbours, POINTS3D
import sys
import numpy as np
from binary_search_function import inverse
from pynverse import inversefunc
from itertools import product
import random



def flow_hash(open_state):
    n = len(open_state)
    coords = list(product(range(n), range(n), range(n)))
    remaining = coords
    res = {}
    def valid(neigh):
        r,c, z = neigh # z = depth as in zorder
        return (0<= r < n) and (0 <=c < n) and (0 <= z <n)
    def get(coord):
        if valid(coord):
            return res.get(coord, None)
        return None
    def set(coord, value):
        if valid(coord):
            res[coord] = value
    def any_true_neigh(coord):
        neighs = neighbours(coord, points=POINTS3D)
        for neigh in neighs:
            if get(neigh) == True:
                return True
        return None
    def nb_false_neighbours(coord):
        return sum([get(neigh) == False for neigh in neighbours(coord, points=POINTS3D)])
    def nb_valid_neigbours(coord):
        return sum([valid(neigh) for neigh in neighbours(coord, points=POINTS3D)])
    def calc_for(coord):
        i, j,k = coord
        if i == 0:
            set(coord, open_state[i][j][k])
            return
        if open_state[i][j][k] == False:
            set(coord, False)
            return
        if any_true_neigh(coord) == True:
            set(coord, True)
            return 
        if nb_false_neighbours(coord) == nb_valid_neigbours(coord):
            set(coord, False)
            return
    while True:
        prev_rem = len(remaining)
        for coord in remaining:
            calc_for(coord)
        remaining = [coord for coord in coords if coord not in res.keys()]
        if not(prev_rem > len(remaining)):
           break 
    # print('remaining', remaining)
    # print(remaining[0])
    # nes = neighbours(remaining[0], points=POINTS3D)
    # print(nb_false_neighbours(remaining[0]))
    # print(nb_valid_neigbours(remaining[0]))
    # for n in nes:
    #     print(n, res.get(n,None))
    return as_matrix3d(res, n)

def as_matrix3d(hashed_coord,n):
    res = np.full([n,n,n], False, np.bool_)
    for coord in hashed_coord:
        res[coord] = hashed_coord[coord]
    return res

    

def percolates(open_state):
    flw = flow_hash(open_state)
    return flw[-1].any()

def experiment(n, prob, nb_trials):
    success = 0
    return sum([percolates(rand_bool_matrix_3d(n,n,n,prob)) for i in range(nb_trials)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Percolation for a random cube')
    parser.add_argument('n', type=int, help='number of rows')
    parser.add_argument('p', type=float, help='probability for the cell be True in the matrix cube')
    parser.add_argument('--estimate-threshold', help='estimate the threshold of percolates', action='store_true')
    parser.add_argument('--nb-trials', type=int, help='number of times the experiment must be carried out')
    args = parser.parse_args()
    n = args.n
    p = args.p
    nb_trials = args.nb_trials

    matr = rand_bool_matrix_3d(n,n,n,p)
    # pprint(matr)
    f=flow_hash(matr)
    # pprint(f)
    # print(percolates(matr))
    # pprint(matr)
    # res = flow_hash(matr)
    # pprint(res)
    if nb_trials is None:
        nb_trials = 100

    def perc_func(p):
        success = experiment(n, p, nb_trials)
        return success/nb_trials


    NBINTERV = 11
    prob_of_success = [0] * NBINTERV
    probs = np.linspace(0,1,NBINTERV)
    for i, p in enumerate(probs):
        success = experiment(n, p, nb_trials)
        prob_of_success[i] = success /nb_trials
        print(success, nb_trials, success/nb_trials)
    print(prob_of_success)
    fig, ax = plt.subplots()
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.title('Probability of percolation nb_sites :' + str(n) + '³' + ' nb_trials: ' + str(nb_trials))
    plt.xlabel('site vacancy probability')
    plt.ylabel('percolation probability')
    colors = ['green' if p > 0.5 else 'red' for p in prob_of_success]
    plt.scatter(probs,prob_of_success,color=colors)
    plt.show()
    if args.estimate_threshold:
        print('Estimating threshold value...')
        a = inversefunc(perc_func, y_values=0.5, domain=[0.3,0.8])
        b = inverse(perc_func,0.5,0.3,0.8)
        print('Threshold value using pynverse', a)
        print('Threshold value is', b)



