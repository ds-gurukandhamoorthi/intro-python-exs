from Turtle import Turtle
import argparse
from math import sin, radians

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a pointed start')
    parser.add_argument('n', type=int, help='number of sides of the star : odd number')
    args = parser.parse_args()
    n = args.n
    # t = Turtle(0.5,0.1, 180/n)
    t = Turtle(0.5,0.1, 180/n*6)
    size = sin(radians(180/n))
    for i in range(n):
        t.go_forward(size)
        t.turn_left(-360/n*2)
    print(t._lines)
    t.draw()
