import randomWalk
import sys
import random

POINTS = randomWalk.POINTS
def oneOf(array):
    "Chooses a single random element from an array"
    return random.sample(array,1)[0]

def printMatrix(matr):
    for row in matr:
        for v in row:
            toprint = 1 if v else 0
            print(toprint,end='')
        print('')

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

def selfAvoidHappened(n):
    "Tells us if self avoidance happened during the trial for n*n matrix"
    visited = [ [ False]*n  for j in range(n)]
    def isVisited(coord):
        return visited[coord[0]][coord[1]]
    def setVisited(coord):
        visited[coord[0]][coord[1]] = True
    def isOutside(coord):
        return not (0<=coord[0]<=(n-1) and 0<=coord[1]<=(n-1))
    def isDeadEnd(coord):
        neighs = neighbours(coord)
        for point in neighs:
            if isOutside(point) or not isVisited(point):
                return False
        return True
    def filterNeighboursVisitableOrOutside(neighs):
        res = []
        for point in neighs:
            if isOutside(point) or not isVisited(point):
                res+=[point]
        return res

    coord = (n//2, n//2)
    steps = 0
    box = (coord, coord)
    while True:
        steps += 1
        neighs = filterNeighboursVisitableOrOutside(neighbours(coord))
        if(isDeadEnd(coord)):
            return (False, steps, calcArea(box))
        else:
            coord = oneOf(neighs)
            box = boundingRectangle(box, coord)
            if(isOutside(coord)):
                return (True, steps, calcArea(box))
            setVisited(coord)


def addCoords(coord1,coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1])

def addCoords3D(coord1,coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1], coord1[2],coord2[2])

def boundingRectangle(box, coord):
    "Given ((xmin, ymin),(xmax,ymax)) and (x,y) returns the new bounding box"
    ((xmin, ymin),(xmax,ymax)) = box
    (x,y) = coord
    return ((min(xmin,x), min(ymin,y)),(max(xmax,x),max(ymax,y)))

def calcArea(box):
    "Given ((x1, y1),(x2,y2)) calculate the area"
    ((x1, y1),(x2,y2)) = box
    return abs(x2-x1) * abs(y2-y1)

def limitlessSelfAvoid():
    def isVisited(coord):
        return visited.get(coord,False)
    def filterNeighboursVisitable(neighs):
        res = []
        for point in neighs:
            if not isVisited(point):
                res+=[point]
        return res
    coord = (0,0)
    steps = 0
    visited = {}
    while True:
        # print(coord, steps, visited)
        steps += 1
        visited[coord] = True
        neighs = filterNeighboursVisitable(neighbours(coord))
        if len(neighs) == 0:
            return steps
        coord = oneOf(neighs)

POINTS3D = ((0,0,-1), (0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))
def limitlessSelfAvoid3D():
    def isVisited(coord):
        return visited.get(coord,False)
    def filterNeighboursVisitable(neighs):
        res = []
        for point in neighs:
            if not isVisited(point):
                res+=[point]
        return res
    coord = (0,0,0)
    steps = 0
    visited = {}
    while True:
        # print(coord, steps, visited)
        steps += 1
        visited[coord] = True
        neighs = filterNeighboursVisitable(neighbours3D(coord, POINTS3D))
        if len(neighs) == 0:
            return steps
        coord = oneOf(neighs)


if __name__ == "__main__":
   assert(addCoords((2,3),(7,11))==(9,14))
   # print(POINTS)

   n = int(sys.argv[1])
   nbTrials = int(sys.argv[2])

   deadEnds = 0
   deadEndPathsLength = 0
   escapePathsLength = 0
   deadEndArea = 0
   escapeArea = 0
   for i in range(nbTrials):
       (success, pathLength, area) = selfAvoidHappened(n)
       if not success:
           deadEnds += 1
           deadEndPathsLength += pathLength
           deadEndArea += area
       else:
           escapePathsLength += 1
           escapeArea += area

       
   print(str(100*deadEnds/nbTrials) + "%")
   print("DeadEnds")
   if deadEnds > 0:
       print(deadEnds/nbTrials, deadEndPathsLength / deadEnds, deadEndArea/nbTrials)
   nbEscapes = nbTrials - deadEnds
   print("Escapes")
   if nbEscapes > 0:
       print(nbEscapes/nbTrials, escapePathsLength / nbEscapes, escapeArea/nbTrials)
    
   print(boundingRectangle(((0,0),(5,5)),(3,3)))
   print(boundingRectangle(((0,0),(5,5)),(-3,-3)))
   print(boundingRectangle(((0,0),(5,5)),(9,9)))
   print(boundingRectangle(((0,0),(5,5)),(-3,9)))
   print(calcArea(((0,0),(5,5))))
   print(calcArea(((1,1),(5,5))))
   print(limitlessSelfAvoid())

   nbTrials = 50
   for i in range(0,nbTrials):
       steps = 0
       steps += limitlessSelfAvoid()
   print(steps/nbTrials)

   print(limitlessSelfAvoid3D())

