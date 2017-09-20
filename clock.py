
import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np
from math import cos, sin
from drawing_utils import draw_graph
import datetime




def as_clock_angles(hour, mins, secs):
    def subdivide_circle(parts, val):
        return (2*math.pi/parts) * (val % parts)
    def clockwise(angle):
        return math.pi/2 - angle
    def get_angle(parts, val):
        return clockwise(subdivide_circle(parts, val))
    return (get_angle(12, hour + mins/60), get_angle(60, mins), get_angle(60, secs))

def clockhand_coords(hour, mins, secs):
    hang, mang, sang = as_clock_angles(hour, mins, secs)
    return (cartesian_coord(0.6,hang), cartesian_coord(0.8, mang), cartesian_coord(0.9,sang))

def getHMS():
    dt = datetime.datetime.now()
    return (dt.hour, dt.minute, dt.second)

if __name__ == "__main__":
    stddraw.setXscale(-1,1)
    stddraw.setYscale(-1,1)
    while True:
        print(getHMS())
        stddraw.clear()
        hhand, mhand, shand = clockhand_coords(*getHMS())

        stddraw.line(0,0,*hhand)
        stddraw.line(0,0,*mhand)
        stddraw.line(0,0,*shand)
        stddraw.show(1000)











