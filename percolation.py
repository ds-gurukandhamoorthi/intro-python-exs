from matrixutils import rand_bool_matr
from pprint import pprint
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import argparse
from rle import rle, rle_to_array
from collections import Counter
from matrixutils import transpose
from geomutils import neighbours
import sys
import numpy as np
from binary_search_function import inverse
from pynverse import inversefunc

RESTRICTED_NEIGH_POINTS = ((0,1),(0,-1),(1,0))

def valid_neigbours(coord, max_lines,max_col):
    def valid(neigh):
        l,c = neigh
        return (0<= l < max_lines) and (0 <=c < max_col)
    neighs=neighbours(coord)
    return [neigh for neigh in neighs if valid(neigh)]


def flow_vertical_only(open_state):
    res = [open_state[0]]
    for i,row in enumerate(open_state[1:]):
        prev=res[i]
        res += [[open_prev and open_row for open_prev, open_row in zip(prev, row)]]
    return res

def flow_hash(open_state, direct_only=False):
    n = len(open_state)
    coords = [(i,j) for i in range(n) for j in range(n)]
    remaining = coords
    res = {}
    def valid(neigh):
        l,c = neigh
        return (0<= l < n) and (0 <=c < n)
    def get(coord):
        if valid(coord):
            return res.get(coord, None)
        return None
    def set(coord, value):
        if valid(coord):
            res[coord] = value
    def any_true_neigh(coord):
        if direct_only == False: 
            neighs = neighbours(coord)
        else:
            neighs = neighbours(coord, points=RESTRICTED_NEIGH_POINTS)
        for neigh in neighs:
            if get(neigh) == True:
                return True
        return None
    def nb_false_neighbours(coord):
        return sum([get(neigh) == False for neigh in neighbours(coord)])
    def nb_valid_neigbours(coord):
        return sum([valid(neigh) for neigh in neighbours(coord)])
    def calc_for(coord):
        i, j = coord
        if i == 0:
            set(coord, open_state[i][j])
            return
        if open_state[i][j] == False:
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
    return as_matrix(res, n)

def as_matrix(hashed_coord,n):
    res = [[None]*n for i in range(n)]
    for x,y in hashed_coord:
        res[x][y] = hashed_coord[(x,y)]
    return res







def flow_(open_state):
    res = [open_state[0]]
    for i,row in enumerate(open_state[1:]):
        prev=res[i]
        this = [None] * len(prev)
        for i, (open_prev, open_row) in enumerate(zip(prev, row)):
            if open_row == False:
                this[i] = False
            elif open_prev is None: 
                pass
            elif open_prev == True:
                this[i] = True
        res += [this]
    res = flow_horiz_matrix(res)
    res = flow_vertic_matrix(res)
    res = flow_horiz_matrix(res)
    res = flow_vertic_matrix(res)
    return res

def flow_horiz_matrix(matr):
    return [flow_horiz(row) for row in matr]

def flow_vertic_matrix(matr):
    return transpose(flow_horiz_matrix(transpose(matr)))

def flow_horiz(row):
    count_types = rle(row)
    nb_true_neighbours = Counter()
    for i, (count, type_) in enumerate(count_types):
        if type_ == True:
            nb_true_neighbours[i-1] += 1
            nb_true_neighbours[i+1] += 1
    for i, (count, type_) in enumerate(count_types):
        if nb_true_neighbours[i] > 0:
            if count_types[i][1] is None:
                count_types[i] = (count, True) #now  count_types is no more a true rle... as it can have (2,True) followed by (1, True ) instead of (3, True)
    return rle_to_array(count_types)
    

def percolates(open_state, direct_only=False):
    flw = flow_hash(open_state, direct_only)
    return any(flw[-1])

def percolatesv(open_state):
    flw = flow_vertical_only(open_state)
    return any(flw[-1])

def get_shapes_for(matr):
    lst_squares = []
    n = len(matr)
    flw = flow_hash(matr)
    for i, row in enumerate(flw):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            if cell == False:
                lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor='black')]
            if flw[i][j] == True:
                lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor='blue')]
    return lst_squares

def ascii_text(matr):
    lst_squares = []
    n = len(matr)
    flw = flow_hash(matr)
    for i, row in enumerate(flw):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            if cell == False:
                print('1', end='')
            elif flw[i][j] == True:
                print('*', end='')
            else:
                print('0', end='')
        print('')

def experiment(n, prob, nb_trials, direct_only=False):
    success = 0
    return sum([percolates(rand_bool_matr(n,prob), direct_only) for i in range(nb_trials)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Percolation for a random matrix')
    parser.add_argument('n', type=int, help='dimension of the square matrix')
    # parser.add_argument('p', type=float, help='probability for the cell be True in the matrix')
    parser.add_argument('--nb-interval-prob', type=int, help='number of interval for the probabilities')
    parser.add_argument('--nb-trials', type=int, help='number of times the experiment must be carried out')
    parser.add_argument('--estimate-threshold', help='estimate the threshold of percolates', action='store_true')
    parser.add_argument('--adaptive', help='EXPERIMENTAL:feature make the intervals based on xaxis rather than the yaxis', action='store_true')
    parser.add_argument('--ascii-with-prob', type=float, help='given the prob draw ascii with the given prob')
    parser.add_argument('--directed', help='help for ', action='store_true')
    args = parser.parse_args()
    n = args.n
    directed = args.directed
    NBINTERV = args.nb_interval_prob
    nb_trials = args.nb_trials
    # p = args.p
    # matr = rand_bool_matr(n,p)
    # pprint(matr)
    # res = flow_hash(matr)
    # pprint(res)
    if directed is None:
        directed = False

    if args.ascii_with_prob:
        p=args.ascii_with_prob
        matr = rand_bool_matr(n,p)
        ascii_text(matr)
        sys.exit(0)


    fig, ax = plt.subplots()
    # ax.set_xlim(0, n)
    # ax.set_ylim(0, n)
    # for ptch in get_shapes_for(matr):
    #     ax.add_patch(ptch)
    # plt.axis('off')
    # fig.savefig('perc.png', dpi=90)
    # plt.show()
    if nb_trials is None:
        nb_trials = 100
    if NBINTERV is None:
        NBINTERV = 11



    def perc_func(p):
        success = experiment(n, p, nb_trials)
        return success/nb_trials
    prob_of_success = [0] * NBINTERV
    probs = np.linspace(0,1,NBINTERV)
    res_probs = np.linspace(0,1,NBINTERV)
    if args.adaptive == True:
        probs=[]
        for y in res_probs:
            probs+= [inversefunc(perc_func, y_values=y, domain=[0,1])]
        print(probs)
    for i, p in enumerate(probs):
        success = experiment(n, p, nb_trials, directed)
        prob_of_success[i] = success /nb_trials
        print(success, nb_trials, success/nb_trials)
    print(prob_of_success)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.title('Probability of percolation nb_sites :' + str(n) + ' nb_trials: ' + str(nb_trials))
    plt.xlabel('site vacancy probability')
    plt.ylabel('percolation probability')
    colors = ['green' if p > 0.5 else 'red' for p in prob_of_success]
    plt.scatter(probs,prob_of_success,color=colors)
    plt.show()
    if args.estimate_threshold:
        print('Estimating threshold value...')
        a = inversefunc(perc_func, y_values=0.5, domain=[0.4,0.6])
        b = inverse(perc_func,0.5,0.4,0.6)
        print('Threshold value using pynverse', a)
        print('Threshold value is', b)




