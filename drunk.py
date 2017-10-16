from Turtle import Turtle
import argparse
from math import sin, radians
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Drunken turtle : study of brownian motion')
    parser.add_argument('step_size', type=float, help='size of each step')
    parser.add_argument('nb_steps', type=int, help='number of steps')
    args = parser.parse_args()
    step_size = args.step_size
    nb_steps = args.nb_steps
    t = Turtle(0.5,0.5, 0)
    for i in range(nb_steps):
        t.turn_left(random.random()*360)
        t.go_forward(step_size)
    t.draw()
