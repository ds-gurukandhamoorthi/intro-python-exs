import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians, pi
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc
from distance import euclideanDist
from collections import Counter
from colorutils import similar


def count_colors(counter, color):
    if len(counter) == 0:
        counter[color] += 1
        return counter
    for clr in counter:
        if similar(clr, color, 1/15):
            counter[clr] += 1
            return counter
    counter[color] += 1
    return counter


def dominant_color(img_array):
    shp = img_array.shape
    colors = Counter()
    for i, row in enumerate(img_array):
        for j, clr in enumerate(row):
            clr = tuple(clr)
            colors = count_colors(colors, clr)
    return colors.most_common(5)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find clusters in an image')
    parser.add_argument('filename',  help='name of the image file')
    args = parser.parse_args()
    filename = args.filename

    im = mpimg.imread(filename)
    d = dominant_color(im)
    print(d)

