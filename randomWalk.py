import sys
import random
from geomutils import POINTS



def randomStep(coord):
    r = random.randrange(0,4)
    step = POINTS[r]
    return (coord[0]+step[0],coord[1]+step[1])


def countSteps(n):
    coord = (0,0)
    steps = 0
    while coord[0] < n and coord[1] < n:
        coord = randomStep(coord)
        steps+=1
    return steps

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(countSteps(n))


        

        
