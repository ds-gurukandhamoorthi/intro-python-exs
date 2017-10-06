from matrixutils import rand_bool_matr
from pprint import pprint
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib.collections
import argparse
from rle import rle, rle_to_array
from collections import Counter
from matrixutils import transpose, dimen
from geomutils import neighbours, POINTS
import sys
import numpy as np
from binary_search_function import inverse
from pynverse import inversefunc
from printBoolArray import get_dot_shapes_for
from itertools import product

RESTRICTED_NEIGH_POINTS = ((0,1),(0,-1),(1,0))
TRIANGULAR_GRID_POINTS = POINTS + ((-1,1),(1,-1))

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

def flow_hash(open_state, direct_only=False, triangular_grid=False):
    nr, nc = dimen(open_state)
    # coords = [(i,j) for i in range(nr) for j in range(nc)]
    coords = list(product(range(nr), range(nc)))
    remaining = coords
    res = {}
    def valid(neigh):
        r,c = neigh
        return (0<= r < nr) and (0 <=c < nc)
    def get(coord):
        if valid(coord):
            return res.get(coord, None)
        return None
    def set(coord, value):
        if valid(coord):
            res[coord] = value
    def any_true_neigh(coord):
        if direct_only == True: 
            neighs = neighbours(coord, points=RESTRICTED_NEIGH_POINTS)
        elif triangular_grid == True:
            neighs = neighbours(coord, points=TRIANGULAR_GRID_POINTS)
        else:
            neighs = neighbours(coord)
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
    return as_matrix(res, nr, nc)

def as_matrix(hashed_coord,nr, nc):
    res = [[None]*nc for i in range(nr)]
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
    

def percolates(open_state, direct_only=False,triangular_grid=False):
    flw = flow_hash(open_state, direct_only,triangular_grid)
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

def experiment(nr,nc, prob, nb_trials, direct_only=False, triangular_grid=False):
    success = 0
    return sum([percolates(rand_bool_matr(nr,nc,prob), direct_only, triangular_grid) for i in range(nb_trials)])

def experiment_vertical_only(nr,nc, prob, nb_trials):
    success = 0
    return sum([percolatesv(rand_bool_matr(nr,nc,prob)) for i in range(nb_trials)])

def show_bond_perc(matr):
    n = len(matr)
    flw = flow_hash(matr)
    lst_lines = []
    for i, row in enumerate(flw):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            if cell == True:
                if j+1 < n and flw[i][j+1] and x+1 < n :
                    lst_lines += [[(x,y),(x+1,y)]]
                if i+1 < n and flw[i+1][j] and y-1 >=0 :
                    lst_lines += [[(x,y),(x,y-1)]]
    lc = matplotlib.collections.LineCollection(lst_lines)
    fig, ax = plt.subplots()
    ax.add_collection(lc)


    lst_dots = get_dot_shapes_for(matr)
    ax.set_xlim(-1,n+1)
    ax.set_ylim(-1,n+1)
    for ptch in lst_dots:
        ax.add_patch(ptch)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Percolation for a random matrix')
    parser.add_argument('n', type=int, help='number of rows')
    parser.add_argument('m', type=int, help='number of columns')
    # parser.add_argument('p', type=float, help='probability for the cell be True in the matrix')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('--nb-interval-prob', type=int, help='number of interval for the probabilities')
    parser.add_argument('--nb-trials', type=int, help='number of times the experiment must be carried out')
    parser.add_argument('--estimate-threshold', help='estimate the threshold of percolates', action='store_true')
    parser.add_argument('--adaptive', help='EXPERIMENTAL:feature make the intervals based on xaxis rather than the yaxis', action='store_true')
    parser.add_argument('--ascii-with-prob', type=float, help='given the prob draw ascii with the given prob')
    group.add_argument('--directed', help=' ', action='store_true')
    group.add_argument('--triangular-grid', help='if the grid is triangular (6 neighbours)', action='store_true')
    group.add_argument('--vertical-only', help='help for ', action='store_true')
    parser.add_argument('--bond', help='edges of th grid provides connectivity', action='store_true')
    args = parser.parse_args()
    n = args.n
    m = args.m
    directed = args.directed
    triangular_grid = args.triangular_grid
    NBINTERV = args.nb_interval_prob
    nb_trials = args.nb_trials
    # p = args.p
    # matr = rand_bool_matr(n,p)
    # pprint(matr)
    # res = flow_hash(matr)
    # pprint(res)
    if directed is None:
        directed = False
    if triangular_grid is None:
        triangular_grid = False
    if triangular_grid:
        n+=1
        m+=1

    if args.ascii_with_prob:
        p=args.ascii_with_prob
        matr = rand_bool_matr(n,m,p)
        ascii_text(matr)
        sys.exit(0)
    
    if args.vertical_only:
        NBINTERV = 11
        nb_trials = 1000
        probs = np.linspace(0,1,NBINTERV)
        prob_of_success = [0] * NBINTERV
        assert n == m #we only know theoritical_vertical_percolation for square matrices
        for i, p in enumerate(probs):
            theoritical_vertical_percolation = 1-(1-p**n)**n
            success = experiment_vertical_only(n, m, p, nb_trials)
            prob_of_success[i] = success /nb_trials
            print(success, nb_trials, success/nb_trials, theoritical_vertical_percolation)
        sys.exit(0)
    if args.bond:
        n+=1
        m+=1
        matr = rand_bool_matr(n,m,0.7)
        print(matr)
        print(flow_hash(matr))
        show_bond_perc(matr)
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
        success = experiment(n,m, p, nb_trials, triangular_grid=triangular_grid)
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
        success = experiment(n, m, p, nb_trials, directed, triangular_grid)
        prob_of_success[i] = success /nb_trials
        print(success, nb_trials, success/nb_trials)
    print(prob_of_success)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.title('Probability of percolation nb_sites :' + str(n) + '×' + str(m) + ' nb_trials: ' + str(nb_trials))
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
            
                



