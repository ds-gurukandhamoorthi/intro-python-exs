from matrixutils import rand_bool_matr
from pprint import pprint
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import argparse
from rle import rle, rle_to_array
from collections import Counter
from matrixutils import transpose

def flow_vertical_only(open_state):
    res = [open_state[0]]
    for i,row in enumerate(open_state[1:]):
        prev=res[i]
        res += [[open_prev and open_row for open_prev, open_row in zip(prev, row)]]
    return res

def flow(open_state):
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
    flw = flow(open_state)
    return any(flw[-1])

def percolatesv(open_state):
    flw = flow_vertical_only(open_state)
    return any(flw[-1])

def get_shapes_for(matr):
    lst_squares = []
    n = len(matr)
    flw = flow(matr)
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
    return sum([percolatesv(rand_bool_matr(n,prob)) for i in range(nb_trials)])


if __name__ == "__main__":
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
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for ptch in get_shapes_for(matr):
        ax.add_patch(ptch)
    plt.axis('off')
    # plt.show()
    nb_trials = 1000
    success = experiment(n, p, nb_trials)
    print(success, nb_trials, success/nb_trials)
    pprint(flow(matr))
    fig.savefig('perc.png', dpi=90)
