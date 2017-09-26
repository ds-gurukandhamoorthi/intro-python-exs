import sys
import math
sys.path.append('../')
import stddraw
import random
from functools import partial
from tuple_utils import swp



def translate(trans, coord):
    "Translate (a, b) -> (x + a, y+b)"
    return (coord[0]+ trans[0],coord[1]+ trans[1])

def shift(array, n):
    return array[n:] + array[:n]

def addNum(num, array):
    return [num + x for x in array]

def fill(x,y, width, height,color):
    stddraw.setPenColor(color)
    stddraw.filledRectangle(x,y, width, height)
    
def draw_diamond(x,y, width, height, color):
    tx = partial(addNum, x)
    ty = partial(addNum, y)
    stddraw.setPenColor(color)
    stddraw.filledPolygon(tx([width/2,width,width/2,0]),ty([0,height/2,height,height/2]))

def four_squares(x,y, width, height,color):
    stddraw.setPenColor(color)
    t = partial(translate,(x,y))
    geom = (width/4, height/4)
    stddraw.filledRectangle(*t((0,0)), *geom)
    stddraw.filledRectangle(*t((0,height*3/4)), *geom)
    stddraw.filledRectangle(*t((width*3/4,0)), *geom)
    stddraw.filledRectangle(*t((width*3/4,height*3/4)), *geom)

def draw_x(x,y, width, height,color):
    tx = partial(addNum, x)
    ty = partial(addNum, y)
    stddraw.setPenColor(color)
    xcoords = tx([width/4, width, width *3/4, 0])
    ycoords = ty([0, height*3/4, height, height*1/4])
    stddraw.filledPolygon(xcoords, ycoords)
    stddraw.filledPolygon(xcoords, shift(ycoords,-2))

def draw_plus(x,y, width, height,color):
    stddraw.setPenColor(color)
    t = partial(translate,(x,y))
    geom_h = (width, height/2)
    geom_v = (width/2, height)
    stddraw.filledRectangle(*t((0,height/4)), *geom_h)
    stddraw.filledRectangle(*t((width/4,0)), *geom_v)



def draw_design1(x,y, width, height,color, dark=stddraw.BLACK, dull=stddraw.WHITE):
    fill(x,y, width, height,dark)
    draw_x(x,y, width, height,dull)
    draw_plus(x,y, width, height,dark)
    draw_diamond(x,y, width, height, color)

def draw_design2(x,y, width, height,color, dark=stddraw.BLACK, dull=stddraw.WHITE):
    fill(x,y, width, height,dark)
    draw_x(x,y, width, height,dull)
    draw_diamond(x,y, width, height, color)

def draw_design3_(x,y, width, height,color, dark=stddraw.BLACK, dull=stddraw.WHITE):
    fill(x,y, width, height,dark)
    draw_diamond(x,y, width, height, color)
    four_squares(x,y, width, height,dull)

def draw_design3(x,y, width, height,color, dark=stddraw.BLACK, dull=stddraw.WHITE):
    fill(x,y, width, height,dull)
    draw_plus(x,y, width, height,dark)
    draw_diamond(x,y, width, height, color)

def draw_design4(x,y, width, height,color, dark=stddraw.BLACK, dull=stddraw.WHITE):
    fill(x,y, width, height,dark)
    draw_x(x,y, width, height,dull)
    four_squares(x,y, width, height,color)
    draw_diamond(x,y, width, height, color)




if __name__ == "__main__":

    stddraw.setXscale(-10, 20)
    stddraw.setYscale(-10, 20)
    draw_design3(-10,-5,10,10, stddraw.GRAY, stddraw.RED, stddraw.BLUE)
    draw_design3(10,5,10,10, stddraw.GRAY, stddraw.RED, stddraw.BLUE)




    stddraw.show()

