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

while True:
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(0)
