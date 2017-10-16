import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians, pi
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc
from distance import euclideanDist
from collections import Counter
from colorutils import similar, are_compatible


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
    return colors.most_common(1)[0][0]

def get_compatible_pixel_coords(img_array, bg_color):
    shp = img_array.shape
    res = []
    for i, row in enumerate(img_array):
        for j, pxl in enumerate(row):
            if are_compatible(pxl, bg_color):
                res += [(i,j)]
    return res

def draw_clusters(img_array, lst_coords):
    shp = img_array.shape
    res = np.zeros(shp)
    for i, row in enumerate(img_array):
        for j, pxl in enumerate(row):
            if (i,j) not in lst_coords:
                res[i,j] = img_array[i,j]
    return res




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find clusters in an image')
    parser.add_argument('filename',  help='name of the image file')
    args = parser.parse_args()
    filename = args.filename

    im = mpimg.imread(filename)
    d = dominant_color(im)
    print(d)
    l = get_compatible_pixel_coords(im, d)
    print(len(l),l)
    
    clus = draw_clusters(im, l)
    mpimg.imsave('tes.png', clus)



