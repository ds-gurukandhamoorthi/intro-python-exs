import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
import numpy as np


n = int(sys.argv[1])
p = float(sys.argv[2])
minradius = float(sys.argv[3])
maxradius = float(sys.argv[4])

stddraw.setXscale(0,1)
stddraw.setYscale(0,1)
for i in range(n):
    if random.random() < p:
        stddraw.setPenColor(stddraw.RED)
    else:
        stddraw.setPenColor(stddraw.BLUE)
    x, y = random.random(), random.random()
    r = random.uniform(minradius, maxradius)
    stddraw.filledCircle(x, y, r)


stddraw.show()

