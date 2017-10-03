from matrixutils import rand_bool_matr
from pprint import pprint
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import argparse

def flow_vertical_only(open_state):
    res = [open_state[0]]
    for i,row in enumerate(open_state[1:]):
        prev=res[i]
        res += [[open_prev and open_row for open_prev, open_row in zip(prev, row)]]
    return res


def percolatesv(open_state):
    flw = flow_vertical_only(open_state)
    return any(flw[-1])

def get_shapes_for(matr):
    lst_squares = []
    n = len(matr)
    flw = flow_vertical_only(matr)
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
    for ptch in get_shapes_for(flow_vertical_only(matr)):
        ax.add_patch(ptch)
    plt.axis('off')
    # plt.show()
    nb_trials = 1000
    success = experiment(n, p, nb_trials)
    print(success, nb_trials, success/nb_trials)
