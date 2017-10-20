import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer

def hilbert(n):
    return lindenmayer('L', {'L':'-RF+LFL+FR-', 'R':'+LF-RFR-FL+'}, n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a space-filling Hilbert Curve')
    parser.add_argument('n', type=int, help='order of the Hilbert curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0.5, 0.5, -90)
    t = lindenmayer_turtle(hilbert(n), step_size, turt)
    print(hilbert(n))
    t.draw()

