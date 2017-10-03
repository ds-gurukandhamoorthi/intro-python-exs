import matplotlib.pyplot as plt
import numpy
from math import cos, sin
import math
import matplotlib.collections
import matplotlib.patches as patches
from geomutils import rotation_matrix
from distance import euclideanDist
from array_utils import group2
import argparse

def new_branches(stem):
    res = []
    ang1, ang2 = math.pi/3, -math.pi/7
    ang3 = (ang1 + ang2) /2
    res += rotate(stem, ang1, 0.4)
    res += rotate(stem, ang2, 0.4)
    res += rotate(stem, ang3, 0.2)
    return res

def rotate(segment, angle, scale = 1):
    point1, point2 = segment
    diff = numpy.subtract(point2, point1)  
    scaled_diff = numpy.multiply(diff, scale)
    rotation = rotation_matrix(angle)
    rotated = numpy.dot(rotation, scaled_diff)
    return [point2,tuple(numpy.add(rotated, point2))]

def recursive_trees_of_order(stems, n):
    if n == 0:
        return stems
    res = []
    for stem in group2(recursive_trees_of_order(stems, n-1)):
        res += new_branches(stem)
    return res

def recursive_trees(stems, n):
    res = []
    for i in range(n+1):
        res += recursive_trees_of_order(stems, i)
    return res




if __name__ == "__main__":
    start, end = (0,0), (0,1)
    stems = [start, end]
    length = euclideanDist(start, end)
    c = patches.Circle(end,length, fill=None)

    parser = argparse.ArgumentParser(description='Draw recursive trees')
    parser.add_argument('n', type=int, help='order of the recursive tree')
    args = parser.parse_args()
    n = args.n
    lines = group2(recursive_trees(stems, n))
    fig, ax = plt.subplots()
    ax.set_xlim(-1,2)
    ax.set_ylim(-1,2)
    ax.add_patch(c)
    lc = matplotlib.collections.LineCollection(lines)
    ax.add_collection(lc)
    plt.show()

    
