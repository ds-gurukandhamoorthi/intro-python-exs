from Turtle import Turtle
import argparse
from math import sin, radians

def koch(n, step_size, turtle):
    if n == 0:
        turtle.go_forward(step_size)
        return turtle
    koch(n-1, step_size, turtle)
    turtle.turn_left(60)
    koch(n-1, step_size, turtle)
    turtle.turn_left(-120)
    koch(n-1, step_size, turtle)
    turtle.turn_left(60)
    koch(n-1, step_size, turtle)
    return turtle


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a koch curve')
    parser.add_argument('n', type=int, help='order of the koch curve')
    args = parser.parse_args()
    n = args.n
    size = 1 / (3.0**n)
    turtle = Turtle(0, 0, 0)
    k = koch(n, size, turtle)
    k.draw()

