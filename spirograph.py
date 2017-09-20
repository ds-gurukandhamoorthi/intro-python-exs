
import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np
from math import cos, sin
from drawing_utils import draw_graph


R = float(sys.argv[1])
r = float(sys.argv[2])
a = float(sys.argv[3])

stddraw.setXscale(-2*(R+r),2*(R+r))
stddraw.setYscale(-2*(R+r),2*(R+r))

def spirograph_point(R, r, a, t):
    x = (R + r)*cos(t) - (r+a)*cos((R+r)*t/r)
    y = (R + r)*sin(t) - (r+a)*sin((R+r)*t/r)
    return (x,y)



# stddraw.circle(0,0,n)
angles = np.arange(0, 2*math.pi, 0.01)
points = [ spirograph_point(R, r, a , t) for t in angles]


draw_graph(points, stddraw.RED)






stddraw.show()

