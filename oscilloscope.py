

import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np
from math import cos, sin, radians
from drawing_utils import draw_graph


amp_x = float(sys.argv[1])
amp_y = float(sys.argv[2])
veloc_x = float(sys.argv[3])
veloc_y = float(sys.argv[4])
theta_x = float(sys.argv[5])
theta_y = float(sys.argv[6])

stddraw.setXscale(-2*(amp_y+amp_x),2*(amp_y+amp_x))
stddraw.setYscale(-2*(amp_y+amp_x),2*(amp_y+amp_x))

def oscilloscope_point(amp_x, amp_y, veloc_x, veloc_y, theta_x, theta_y, t):
    x = amp_x * sin(veloc_x * t + radians(theta_x))
    y = amp_y * sin(veloc_y * t + radians(theta_y))
    return (x,y)



# stddraw.circle(0,0,n)
angles = np.arange(0, 2*math.pi, 0.01)
points = [ oscilloscope_point(amp_x, amp_y, veloc_x, veloc_y, theta_x, theta_y, t) for t in angles]


draw_graph(points, stddraw.RED)






stddraw.show()

