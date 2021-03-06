from math import pi, cos, sin
POINTS = ((0,1),(0,-1),(1,0),(-1,0))
POINTS8 = POINTS + ((1,1),(1,-1),(-1,1),(-1,-1))
POINTS3D = ((0,0,-1), (0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))


def add_coords(coord1, coord2):
    return tuple([x+y for x, y in zip(coord1,coord2)])

def sub_coords(coord1, coord2):
    return tuple([x-y for x, y in zip(coord1,coord2)])

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

def rotation_matrix(angle):
    return [[cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]]

def is_valid_coord(coord, shape):
    if len(coord) != len(shape):
        return False
    return all( 0<=x<dim for x, dim in zip(coord,shape))

def lc_to_xy(coord, height):
    l, c = coord
    return (c, height-1-l)

def xy_to_lc(coord, height):
    x, y = coord
    return(height-1-y,x)

if __name__ == "__main__":
    point1 = (1,2)
    point2 = (3,4)
    print( add_coords(point1,point2))
    point1 = (1,2,3)
    point2 = (4,5,6)
    print( add_coords(point1,point2))
    print(neighbours(point1,POINTS3D))







