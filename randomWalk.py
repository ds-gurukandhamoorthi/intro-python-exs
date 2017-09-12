import sys
import random

n = int(sys.argv[1])




def randomStep(coord):
    r = random.randrange(0,4)
    points = ((0,1),(0,-1),(1,0),(-1,0))
    step = points[r]
    return (coord[0]+step[0],coord[1]+step[1])


def countSteps(n):
    coord = (0,0)
    steps = 0
    while coord[0] < n and coord[1] < n:
        coord = randomStep(coord)
        steps+=1
    return steps

print(countSteps(n))


    

    
