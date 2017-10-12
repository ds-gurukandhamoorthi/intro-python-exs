import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians, pi
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc
from distance import euclideanDist



def swirled_coord_cartesian(source, center):
    "swirl coordinate source with the given center"
    angle = -euclideanDist(source, center) *  (pi/256)
    target_x = int((source[0]-center[0])*cos(angle) - (source[1]-center[1])*sin(angle) + center[0])
    target_y = int((source[0]-center[0])*sin(angle) + (source[1]-center[1])*cos(angle) + center[1])
    return target_x, target_y

def swirled(source, center, height):
    "swirl coordinate source with the given center: in a row first... matrix coord"
    source_ = lc_to_xy(source, height)
    target_ = swirled_coord_cartesian(source_, center)
    target = xy_to_lc(target_, height)
    return target



def swirl(img_array, center=None):
    shp = img_array.shape
    if center is None:
        center = (shp[1]-1)/2, (shp[0]-1)/2
    res = np.zeros(shp)
    for i, row in enumerate(res):
        for j, _ in enumerate(row):
            target_coord = swirled((i,j), center, shp[0])
            if is_valid_coord(target_coord, shp[0:2]):
                res[i,j] = img_array[target_coord]
    return res




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rotate a given image')
    parser.add_argument('filename',  help='name of the image file')
    args = parser.parse_args()
    filename = args.filename

    outputfile = os.path.splitext(filename)[0] + '_swirl.png'
    im = mpimg.imread(filename)
    swrld = swirl(im)
    mpimg.imsave(outputfile, swrld)

