import argparse

import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np
from math import cos, sin, radians
from drawing_utils import draw_graph

parser = argparse.ArgumentParser(description='draw oscillocope using Lissajous patterns\n example : 1 1 2 3 20 45  or 1 1 5 3 30 45')
parser.add_argument('amp_x', type=float, help='amplitude x axis')
parser.add_argument('amp_y', type=float, help='amplitude y axis')
parser.add_argument('veloc_x', type=float, help='velocity x axis')
parser.add_argument('veloc_y', type=float, help='velocity y ayis')
parser.add_argument('theta_x', type=float, help='angle in degrees x axis')
parser.add_argument('theta_y', type=float, help='angle in degrees y ayis')
args = parser.parse_args()
amp_x =args.amp_x
amp_y = args.amp_y
veloc_x =  args.veloc_x
veloc_y = args.veloc_y
theta_x = args.theta_x
theta_y = args.theta_y

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

