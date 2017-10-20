import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer

def dragon(n):
    return lindenmayer('FX', {'X': 'X-YF-', 'Y':'+FX+Y'}, n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a dragon curve')
    parser.add_argument('n', type=int, help='order of the dragon curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0.5, 0.5, 0)
    t = lindenmayer_turtle(dragon(n), step_size, turt)
    t.draw()

