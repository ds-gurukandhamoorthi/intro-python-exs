from Turtle import Turtle
import argparse
from math import sin, radians
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Drunken turtle : study of brownian motion')
    parser.add_argument('step_size', type=float, help='size of each step')
    parser.add_argument('nb_steps', type=int, help='number of steps')
    parser.add_argument('nb_turtles', type=int, help='number of turtles')
    args = parser.parse_args()
    step_size = args.step_size
    nb_steps = args.nb_steps
    nb_turtles = args.nb_turtles
    turtles = [None]*nb_turtles
    for t in range(nb_turtles):
        turtles[t] = Turtle(random.random(), random.random(),0)
    for i in range(nb_steps):
        for j in range(nb_turtles):
            turtles[j].turn_left(random.random()*360)
            turtles[j].go_forward(step_size)
    tur = Turtle(0,0,0)
    for t in range(nb_turtles):
        tur.merge(turtles[t])
    tur.draw()


