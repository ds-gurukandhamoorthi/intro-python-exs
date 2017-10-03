from math import pi, cos, sin
POINTS = ((0,1),(0,-1),(1,0),(-1,0))
POINTS3D = ((0,0,-1), (0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))


def add_coords(coord1, coord2):
    return tuple([x+y for x, y in zip(coord1,coord2)])

def neighbours(coord, points=POINTS):
    res = []
    for point in points:
        neigh = add_coords(point,coord)
        res += [neigh]
    return res

def midpoint(p1, p2):
    return tuple([(x + y)/2 for x,y in zip(p1,p2)])

def gen_polygon_coordinates(n=3, scale=1, angle_offset=0):
    angles = (angle_offset + i*(2*pi / n) for i in range(0,n))
    return [(scale*cos(a), scale*sin(a)) for a in angles]

if __name__ == "__main__":
    point1 = (1,2)
    point2 = (3,4)
    print( add_coords(point1,point2))
    point1 = (1,2,3)
    point2 = (4,5,6)
    print( add_coords(point1,point2))
    print(neighbours(point1,POINTS3D))




        

        
