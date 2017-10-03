import math
import matplotlib.pyplot as plt
from geomutils import gen_polygon_coordinates, midpoint
from itertools import combinations

def sierpinski_step(triangle):
    midpoints = [midpoint(*vertices) for vertices in combinations(triangle, 2)]
    print("midpoints", midpoints)
    print(triangle)
    res = []
    return midpoints

def sierpinski_triangles(n):
    res = {}
    if n < 1:
        return res
    if n == 1:
        res[1] = [tuple(gen_polygon_coordinates(3,angle_offset=math.pi/2))]
        return res





if __name__ == "__main__":
    pts = gen_polygon_coordinates(3, angle_offset=math.pi/2)
    print(sierpinski_step(pts))
    pts2=sierpinski_step(pts)


    # pts = sierpinski_triangles(1)[1][0]
    print(pts)
    t1=plt.Polygon(pts, fill=None)
    t2=plt.Polygon(pts2, fill=None)
    fig, ax=plt.subplots()
    plt.axis('off')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    plt.gca().add_patch(t1)
    plt.gca().add_patch(t2)
    plt.show()
