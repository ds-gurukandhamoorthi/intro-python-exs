import randomWalk
import sys
import random

def oneOf(array):
    "Chooses a single random element from an array"
    return random.sample(array,1)[0]

def printMatrix(matr):
    for row in matr:
        for v in row:
            toprint = 1 if v else 0
            print(toprint,end='')
        print('')

POINTS = randomWalk.POINTS
def selfAvoidHappened(n):
    "Tells us if self avoidance happened during the trial for n*n matrix"
    visited = [ [ False]*n  for j in range(n)]
    def isVisited(coord):
        return visited[coord[0]][coord[1]]
    def setVisited(coord):
        visited[coord[0]][coord[1]] = True
    def isOutside(coord):
        return not (0<=coord[0]<=(n-1) and 0<=coord[1]<=(n-1))
    def neighbours(coord):
        res = []
        for point in POINTS:
            neigh = addCoords(point,coord)
            res += [neigh]
        return res
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
    while True:
        neighs = filterNeighboursVisitableOrOutside(neighbours(coord))
        if(isDeadEnd(coord)):
            return False
        else:
            coord = oneOf(neighs)
            if(isOutside(coord)):
                return True
            setVisited(coord)


def addCoords(coord1,coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1])


if __name__ == "__main__":
   assert(addCoords((2,3),(7,11))==(9,14))
   # print(POINTS)

   n = int(sys.argv[1])
   nbTrials = int(sys.argv[2])

   deadEnds = 0
   for i in range(nbTrials):
       if not selfAvoidHappened(n):
           deadEnds += 1
       
   print(str(100*deadEnds/nbTrials) + "%")
