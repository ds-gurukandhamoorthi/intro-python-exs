POINTS = ((0,1),(0,-1),(1,0),(-1,0))
POINTS3D = ((0,0,-1), (0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))

def addCoords(coord1,coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1])

def addCoords3D(coord1,coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1], coord1[2],coord2[2])

def neighbours(coord, points=POINTS):
    res = []
    for point in points:
        neigh = addCoords(point,coord)
        res += [neigh]
    return res

def neighbours3D(coord, points):
    res = []
    for point in points:
        neigh = addCoords3D(point,coord)
        res += [neigh]
    return res




        

        
