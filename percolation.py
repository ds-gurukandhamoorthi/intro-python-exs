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

def flow_hash(open_state):
    n = len(open_state)
    coords = [(i,j) for i in range(n) for j in range(n)]
    remaining = coords
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
        for neigh in neighbours(coord):
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
        if any_true_neigh((i,j)) == True:
            set(coord, True)
            return 
        if nb_false_neighbours(coord) == nb_valid_neigbours(coord):
            set(coord, False)
            return

    res = {}
    for coord in remaining:
        calc_for(coord)
    remaining = [coord for coord in coords if coord not in res.keys()]
    print("remaining", remaining, len(remaining))
    for coord in remaining:
        calc_for(coord)
    print("remaining", remaining, len(remaining))
    print(len(res))
    return as_matrix(res, n)

def as_matrix(hashed_coord,n):
    res = [[None]*n for i in range(n)]
    for x,y in hashed_coord:
        res[x][y] = hashed_coord[(x,y)]
    return res







def connected_to_top(open_state, i, j, partial):
    "For the given coordinates tells if the cell is connected to the top (can the top percolate until this cell)"
    if i == 0:
        return open_state[i][j]
    if open_state[i][j] == False:
        return False
    if partial[i][j-1] == True:
        return True
    if partial[i-1][j] == True:
        return True
    n = len(open_state)
    for l,c in valid_neigbours((i,j), n, n):
        if connected_to_top(open_state, l, c, partial):
            return True
    return False
    # return any ((connected_to_top(open_state, l, c, partial) for l,c in valid_neigbours((i,j), n, n)))

def connect_to_top_inplace(open_state, i , j , partial):
    n = len(open_state)
    if i >= n or i <0 or j >=n or j<0:
        return
    if partial[i][j] is not None:
        return
    if i == 0:
        partial[i][j] = open_state[i][j]
        return
    if open_state[i][j] == False:
        partial[i][j] = False
        return
    if partial[i][j-1] == True:
        partial[i][j] = True
        return
    if partial[i-1][j] == True:
        partial[i][j] = True
        return
    connect_to_top_inplace(open_state, i+1, j, partial)
    connect_to_top_inplace(open_state, i, j+1, partial)
    connect_to_top_inplace(open_state, i, j-1, partial)
    connect_to_top_inplace(open_state, i-1, j, partial)
    



# def flow(open_state):
#     res = [[None]*n for i in range(n)]
#     for i in range(n):
#         connect_to_top_inplace(open_state, 0 , i, res)
#     return res

def flow(open_state):
    res = flow_(open_state)
    for i in range(n):
        for j in range(n):
            if res[i][j] is None:
                connect_to_top_inplace(open_state, i+1, j, res)
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
    

def percolates(open_state):
    flw = flow_hash(open_state)
    return any(flw[-1])

def percolatesv(open_state):
    flw = flow_vertical_only(open_state)
    return any(flw[-1])

def get_shapes_for(matr):
    lst_squares = []
    n = len(matr)
    flw = flow_hash(matr)
    for i, row in enumerate(matr):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            if cell == False:
                lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor='black')]
            if flw[i][j] == True:
                lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor='blue')]
    return lst_squares

def experiment(n, prob, nb_trials):
    success = 0
    return sum([percolates(rand_bool_matr(n,prob)) for i in range(nb_trials)])

if __name__ == "__main__":
    # sys.setrecursionlimit(15000)
    # matr = [
    # [False,True,True,False,True],
    # [False,False,True,True,True],
    # [True,True,False,True,True],
    # [True,False,False,False,True],
    # [False,True,True,True,True]]
    parser = argparse.ArgumentParser(description='Percolation for a random matrix')
    parser.add_argument('n', type=int, help='dimension of the square matrix')
    parser.add_argument('p', type=float, help='probability for the cell be True in the matrix')
    args = parser.parse_args()
    n = args.n
    p = args.p
    matr = rand_bool_matr(n,p)
    pprint(matr)
    pprint(flow_hash(matr))

    # sys.exit(0)
    


    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for ptch in get_shapes_for(matr):
        ax.add_patch(ptch)
    plt.axis('off')
    fig.savefig('perc.png', dpi=90)
    # plt.show()
    nb_trials = 1000
    # sys.exit(0)
    success = experiment(n, p, nb_trials)
    print(success, nb_trials, success/nb_trials)
    pprint(flow(matr))

