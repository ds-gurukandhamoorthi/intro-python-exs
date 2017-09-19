import sys
import math
sys.path.append('../')
import stddraw
import random



stddraw.setXscale(0, 10)
stddraw.setYscale(0, 10)


def draw_diamond():
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledPolygon([5,10,5,0],[0,5,10,5])

def draw_heart():
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledCircle(2.5,7.5,2.5)
    stddraw.filledCircle(7.5,7.5,2.5)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0, 0, 10, 7.5)
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledPolygon([5,10,0],[0,7.5,7.5])

def draw_clubs():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledPolygon([4,6,5],[0,0,5])
    stddraw.filledCircle(5,7.5,2.5)
    stddraw.filledCircle(7.5,4,2.5)
    stddraw.filledCircle(2.5,4,2.5)
    stddraw.filledCircle(5,5,2.5)

def draw_spades():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledPolygon([4,6,5],[0,0,5])
    stddraw.filledPolygon([0,10,5],[5,5,10])
    stddraw.filledCircle(2.5,4,2.68)
    stddraw.filledCircle(7.5,4,2.68)



draw_spades()




stddraw.show()

