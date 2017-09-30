import argparse
from geomutils import midpoint
import matplotlib.pyplot as plt
import matplotlib.collections
import time

def upper_corners(x, y, line_length):
    half = line_length / 2
    return (x-half, y+half), (x+half, y+half)

def lower_corners(x, y, line_length):
    half = line_length / 2
    return (x-half, y-half), (x+half, y-half)


def get_H_shape_lines(uc, lc):
    "return list of points to draw for the H shape given the upper corner and the lower corner"
    return [[midpoint(uc[0], lc[0]), midpoint(uc[1], lc[1])],
    [uc[0],lc[0]],
    [uc[1],lc[1]]]


def htree_lines( x,y, line_length, order):
    points = []
    uc = upper_corners(x, y, line_length)
    lc = lower_corners(x, y, line_length)
    if order > 1:
        for corner in uc + lc:
            points += htree_lines(*corner, line_length/2,order-1)
    points += get_H_shape_lines(uc, lc)
    return points

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw an H-Tree')
    parser.add_argument('order', type=int, help='order of the H-Tree')
    args = parser.parse_args()
    order = args.order
    h = htree_lines(0,0,1,order)
    i = 0
    fig, ax = plt.subplots(1,1)
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    for i in range(1,len(h)//3+1):
        lc = matplotlib.collections.LineCollection(h[:i*3])
        ax.set_title('H- Tree of order ' + str(order))
        ax.add_collection(lc,autolim=True)
        plt.draw()
        plt.pause(1e-17)
        time.sleep(0.1)
    plt.show()
    # print(h)
