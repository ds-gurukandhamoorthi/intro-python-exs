import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer

def gosper_island(n):
    return lindenmayer('LF--RF--LF--RF--LF--RF', {'L':'+F---F+++F', 'R': '---F-F+F'},n)
# +F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw Gosper''s Island')
    parser.add_argument('n', type=int, help='order of the Hilbert curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0.5, 0.5, 0)
    print(gosper_island(n))
    t = lindenmayer_turtle(gosper_island(n), step_size, turt, angle=30)
    strng = '+F---F+++F---F-F+F'

    # t = lindenmayer_turtle(strng, step_size, turt, angle=30)
    t.draw()

