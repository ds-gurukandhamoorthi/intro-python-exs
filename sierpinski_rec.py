import math
import matplotlib.pyplot as plt
from geomutils import gen_polygon_coordinates, midpoint
from itertools import combinations
from array_utils import group3
import argparse

def sierpinski_step(triangle_vertices):
    n = len(triangle_vertices) # 3
    midpoints = [midpoint(*pair_vertices) for pair_vertices in combinations(triangle_vertices, 2)]
    res =[]
    for i, pair_midpoints in enumerate(combinations(midpoints, 2)):
        # res += (*pair_midpoints, triangle_vertices[(i+2)%3])
        res += (*pair_midpoints, triangle_vertices[i])
    return res

def sierpinski_triangles(n):
    if n < 1:
        return []
    if n == 1:
        return tuple(gen_polygon_coordinates(3,angle_offset=math.pi/2))
    prev = sierpinski_triangles(n-1)
    res = []
    for tri in group3(prev):
        res += sierpinski_step(tri)
    return res


def get_list_shapes(list_vertices):
    lst_shapes = []
    for pt in group3(list_vertices):
        shp = plt.Polygon(pt, fill=None)
        lst_shapes += [shp]
    return lst_shapes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw Sierpinski triangles')
    parser.add_argument('n', type=int, help='order of the triangle')
    args = parser.parse_args()
    n = args.n
    pts2 = sierpinski_triangles(n)

    fig, ax=plt.subplots()
    plt.axis('off')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    for shp in get_list_shapes(pts2):
        plt.gca().add_patch(shp)
    plt.show()
