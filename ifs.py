import argparse
import matplotlib.pyplot as plt
from ioutils import readFloatMatrixOrVector
from matrixutils import dot
from numpy.random import choice

def rand_num(n, probs):
    n = choice(range(0,n), size=1, p=probs)[0]
    return n

def transform(point, coef_transf_x, coef_transf_y):
    point_ = point +(1,)
    x = dot(point_,coef_transf_x)
    y = dot(point_,coef_transf_y)
    return (x,y)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Read from stdin and draw iterated function system')
    parser.add_argument('n', type=int, help='number of points')
    args = parser.parse_args()
    n = args.n

    prob_dist = readFloatMatrixOrVector()
    cx = readFloatMatrixOrVector()
    cy = readFloatMatrixOrVector()
    point = (0,0)
    print(prob_dist)
    print(cx)
    print(cy)
    print(point)
    points = []
    for i in range(n):
        r = rand_num(len(cx), prob_dist)
        point = transform(point, cx[r], cy[r] ) #same row for both x, y transf
        points += [point]
    plt.plot(*zip(*points), 'ro', markersize=1)
    plt.show()
