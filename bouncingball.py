import sys
sys.path.append('../')
import stddraw

RADIUS = 0.05
DT = 20.0

stddraw.setXscale(-1.0,1.0)
stddraw.setYscale(-1.0,1.0)

rx = .480
ry = .860
vx = .015
vy = .023

rx_ = None
ry_ = None

stddraw.clear(stddraw.GRAY)
while True:
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy 
    rx = rx + vx
    ry = ry + vy*0.8

    # stddraw.clear(stddraw.GRAY)
    if rx_ is not None and ry_ is not None:
        stddraw.setPenColor(stddraw.GRAY)
        stddraw.filledCircle(rx_,ry_, RADIUS)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.circle(rx_, ry_, RADIUS)
    stddraw.filledCircle(rx, ry, RADIUS)
    rx_ = rx
    ry_ = ry
    stddraw.show(0)
