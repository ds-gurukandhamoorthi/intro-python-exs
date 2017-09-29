import argparse
from geomutils import midpoint
import matplotlib.pyplot as plt
import matplotlib.collections

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
    points += get_H_shape_lines(uc, lc)
    if order > 1:
        for corner in uc + lc:
            points += htree_lines(*corner, line_length/2,order-1)
    return points

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw an H-Tree')
    parser.add_argument('order', type=int, help='order of the H-Tree')
    args = parser.parse_args()
    order = args.order
    h = htree_lines(1,1,2,order)
    lc = matplotlib.collections.LineCollection(h)
    fig, ax = plt.subplots(1,1)
    ax.add_collection(lc,autolim=True)
    ax.autoscale_view()
    ax.set_title('H- Tree of order ' + str(order))
    plt.show()
    # print(h)
