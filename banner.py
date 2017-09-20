
import sys
import math
sys.path.append('../')
import stddraw
import random
from mathutils import cartesian_coord


text = ' '.join(sys.argv[1:])

maxwidth = 10
stddraw.setXscale(0,maxwidth)
stddraw.setYscale(0,maxwidth)
stddraw.setFontSize(60)

i=0
while True:
    if i > maxwidth:
        i = 0
    stddraw.clear()
    stddraw.text(i,5,text)
    stddraw.text(i+maxwidth,5,text)
    stddraw.text(i-maxwidth,5,text)
    i += 0.1
    stddraw.show(60.0)





