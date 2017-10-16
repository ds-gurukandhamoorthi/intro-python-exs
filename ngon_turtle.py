from Turtle import Turtle
import argparse
from math import sin, radians

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw of polygon')
    parser.add_argument('n', type=int, help='number of sides of the polygon')
    args = parser.parse_args()
    n = args.n
    t = Turtle(0.5,0.1, 180/n)
    size = sin(radians(180/n))
    for i in range(n):
        t.go_forward(size)
        t.turn_left(360/n)
    print(t._lines)
    t.draw()
