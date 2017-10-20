import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer

def koch(n):
    return lindenmayer('F', {'F':'F-F+F+F-F'}, n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a koch curve using turtle graphics')
    parser.add_argument('n', type=int, help='order of the koch curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0, 0, 0)
    t = lindenmayer_turtle(koch(n), step_size, turt)
    t.draw()

