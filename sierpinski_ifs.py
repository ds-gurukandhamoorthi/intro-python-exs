import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi
from randomutils import oneOf
from geomutils import midpoint, add_coords, gen_polygon_coordinates


def sierpinski_ifs(vertices = [(0,0), (1,0), (1/2,sqrt(3)/2)], n = 10000, func=None):
    "Generate sierpinski points"
    point = oneOf(vertices)
    res = []
    for i in range(n):
        if func is None:
            point = add_coords(point, oneOf(vertices))
            point = [x / (len(vertices)-1) for x in point] #midpoint is 1/2 that is 1/(3-1)   3 represents the number of vertices...
        else:
            point = func(point, oneOf(vertices)) #if we want to force midpoint for all n. we can use any function that takes two points and return a new one
        res += [point]
    return res
        

if __name__ == "__main__":
    # points = sierpinski_ifs(vertices=gen_polygon_coordinates(5),n=100000, func=midpoint)
    # points = sierpinski_ifs(vertices=gen_polygon_coordinates(13),n=100000, func=add_coords)
    points = sierpinski_ifs(vertices=gen_polygon_coordinates(3),n=100000)
    plt.plot(*zip(*points), 'ro', markersize=1)
    plt.show()
