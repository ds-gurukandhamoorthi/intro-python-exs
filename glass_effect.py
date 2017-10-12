import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians, pi
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc
from distance import euclideanDist
import random


def random_neighbour(coord, shape, radius_pxls):
    def rnd(n):
        return random.randrange(-n, n+1)
    height, width = shape
    x, y = coord
    return (x+rnd(radius_pxls)) % height, (y+rnd(radius_pxls)) % width



def glass_effect(img_array, radius_pxls=5):
    shp = img_array.shape
    res = np.zeros(shp)
    for i, row in enumerate(res):
        for j, _ in enumerate(row):
            target_coord = random_neighbour((i,j), shp[0:2], radius_pxls)
            if is_valid_coord(target_coord, shp[0:2]):
                res[i,j] = img_array[target_coord]
    return res




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Apply glassy blur on a given image')
    parser.add_argument('filename',  help='name of the image file')
    args = parser.parse_args()
    filename = args.filename

    outputfile = os.path.splitext(filename)[0] + '_glassy.png'
    im = mpimg.imread(filename)
    glassy = glass_effect(im, 5)
    mpimg.imsave(outputfile, glassy)

