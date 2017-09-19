import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord


n = int(sys.argv[1])
p = float(sys.argv[2])

stddraw.setXscale(-n-1,n+1)
stddraw.setYscale(-n-1,n+1)



# stddraw.circle(0,0,n)
angles = [ i * 2*(math.pi/n) for i in range(n)]
points = [ cartesian_coord(n, angles[i]) for i in range(n)]

for i in range(n):
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledSquare(*points[i], 0.1)

for i in range(n):
    for j in range(n):
        if random.random() <= p:
            stddraw.setPenColor(stddraw.GRAY)
            stddraw.line(*points[i],*points[j])




stddraw.show()

