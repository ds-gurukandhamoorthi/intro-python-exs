import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np
from drawing_utils import draw_graph


n = int(sys.argv[1])

stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)



# stddraw.circle(0,0,n)
angles = np.arange(0, 2*math.pi, 0.01)
radius_list = [math.sin(n * theta) for theta in angles]
points = [ cartesian_coord(radius, theta) for radius, theta in zip(radius_list, angles)]

print(points)

draw_graph(points, stddraw.RED)






stddraw.show()

