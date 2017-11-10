from matrixutils import rand_bool_matrix_2d
from geomutils import neighbours, POINTS8
import numpy as np
import printBoolArray
import argparse


# we can have negative coordinates... as we merely check for neighbours we don't make elaborate checking   a= [3,4]  -2 is a valid index, -3 is not ... our function would fail for such a case
def valid(coord, dim):
    if len(coord) != len(dim):
        return False
    return all([a < b for a, b in zip(coord, dim)])


def force_lesser_than(coord, dim):
    x, y = coord
    l, c = dim
    return (x % l), (y % c)


def torus_neighbours(coord, dim):
    neighs = neighbours(coord, POINTS8)
    res = []
    for neigh in neighs:
        res += [force_lesser_than(neigh, dim)]
    return res


def get_neighbours_state(matr, coord):
    dim = matr.shape
    neighs = torus_neighbours(coord, dim)
    res = []
    for neigh in neighs:
        res += [matr[neigh]]
    return res


def about_next_life(matr, coord):
    neigh_states = get_neighbours_state(matr, coord)
    nb = sum(neigh_states)
    if matr[coord] == True:
        if nb < 2:
            return False
        if nb in (2, 3):
            return True
        return False
    return nb == 3


def conway(matr):
    res = np.copy(matr)
    for i, row in enumerate(matr):
        for j, cell in enumerate(row):
            res[(i, j)] = about_next_life(matr, (i, j))
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Conway''s game of Life')
    parser.add_argument('n', type=int, help='number of rows')
    parser.add_argument('m', type=int, help='number of columns')
    parser.add_argument('p', type=float, help='probability of life at start')
    parser.add_argument('--nb-steps', type=int, help='number of generations')
    args = parser.parse_args()
    n = args.n
    m = args.m
    p = args.p
    nb_steps = args.nb_steps

    # glider
    # matr = np.array([[False,False,False,False,False],
    #     [False,False,True,False,False],
    #     [False,False,False,True,False],
    #     [False,True,True,True,False],
    #     [False,False,False,False,False]])
    matr = rand_bool_matrix_2d(n, m, p)
    printBoolArray.printMatrix(matr)
    c = matr
    for i in range(nb_steps):
        c = conway(c)
        printBoolArray.printMatrix(c)
