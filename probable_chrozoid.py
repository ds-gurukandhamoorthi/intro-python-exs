import argparse
import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord
from geomutils import gen_polygon_coordinates

parser = argparse.ArgumentParser(description='Draw a chrozoid graph using probability to draw lines')
parser.add_argument('n', type=int, help='number of subdivisions of circle')
parser.add_argument('prob', type=float, help='probability for drawing the line: 0 <= prob <= 1')
args = parser.parse_args()
n = args.n
p = args.prob
if not 0<=p<=1:
    parser.print_help()
    sys.exit(1)


stddraw.setXscale(-n-1,n+1)
stddraw.setYscale(-n-1,n+1)


points = gen_polygon_coordinates(n, scale=n, angle_offset=math.pi/2)

for i in range(n):
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledSquare(*points[i], 0.1)

for i in range(n):
    for j in range(n):
        if random.random() <= p:
            stddraw.setPenColor(stddraw.GRAY)
            stddraw.line(*points[i],*points[j])




stddraw.show()

