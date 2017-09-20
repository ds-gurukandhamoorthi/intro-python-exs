import sys
import math
sys.path.append('../')
import stddraw
import random
from functools import partial
from randomutils import oneOf


from designs import draw_design1, draw_design2, draw_design3, draw_design4


if __name__ == "__main__":
    n = int(sys.argv[1])
    is_checkered = oneOf([True,False])
    stddraw.setXscale(0, n)
    stddraw.setYscale(0, n)

    design=oneOf([draw_design1, draw_design2, draw_design3, draw_design4])
    color = oneOf([stddraw.BLUE,stddraw.GRAY])
    dark = oneOf([stddraw.BLACK, stddraw.RED])
    dull = oneOf([stddraw.WHITE, stddraw.BLUE])
    stddraw.clear(color)

    is_checkered = True

    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0 or not is_checkered:
                design(i,j,1,1, color, dark, dull)




stddraw.show()

