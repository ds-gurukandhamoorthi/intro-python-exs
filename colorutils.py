import numpy as np
import random

def luminance(rgb):
    W_RGB=(0.299, 0.587, 0.114)
    return np.dot(W_RGB, rgb)

def are_compatible(color1, color2, max_color=1):
    "Tells if two colors defined in the range of 0-max_color 0-max_color 0-max_color are compatible"
    return abs(luminance(color1)-luminance(color2)) > (max_color/2)

def as_matplotlib_color(color):
    return tuple(c /255 for c in color)

def rand_color():
    return (random.randrange(255),random.randrange(255),random.randrange(255))
