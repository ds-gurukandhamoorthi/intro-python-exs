import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer


def gosper(n):
    return lindenmayer('L', {'L': 'LF-RF--RF+LF++LFLF+RF-', 'R': '+LF-RFRF--RF-LF++LF+RF'}, n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Draw a space-filling Hilbert Curve')
    parser.add_argument('n', type=int, help='order of the Hilbert curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0.5, 0.5, -90)
    print(gosper(n))
    t = lindenmayer_turtle(gosper(n), step_size, turt, angle=60)
    t.draw()
