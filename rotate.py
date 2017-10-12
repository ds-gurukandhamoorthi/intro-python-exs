import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc



def rotated_coord_cartesian(source, center, angle):
    "rotate coordinate source with the given center and the given angle in radians"
    target_x = int((source[0]-center[0])*cos(angle) - (source[1]-center[1])*sin(angle) + center[0])
    target_y = int((source[0]-center[0])*sin(angle) + (source[1]-center[1])*cos(angle) + center[1])
    return target_x, target_y

def rotated_coord_lc(source, center, angle, height):
    "rotate coordinate source with the given center and the given angle in radians in a row first... matrix coord"
    source_ = lc_to_xy(source, height)
    target_ = rotated_coord_cartesian(source_, center, angle)
    target = xy_to_lc(target_, height)
    return target


# def rotate(img_array,  angle, center=None):
#     shp = img_array.shape
#     if center is None:
#         center = (shp[1]-1)/2, (shp[0]-1)/2
#     res = np.zeros(shp)
#     for i, row in enumerate(img_array):
#         for j, _ in enumerate(row):
#             target_coord = rotated_coord_lc((i,j), center, radians(angle), shp[0])
#             if is_valid_coord(target_coord, shp[0:2]):
#                 res[target_coord] = img_array[i,j]
#     return res

def rotate(img_array,  angle, center=None):
    shp = img_array.shape
    if center is None:
        center = (shp[1]-1)/2, (shp[0]-1)/2
    res = np.zeros(shp)
    for i, row in enumerate(res):
        for j, _ in enumerate(row):
            target_coord = rotated_coord_lc((i,j), center, radians(-angle), shp[0])
            if is_valid_coord(target_coord, shp[0:2]):
                res[i,j] = img_array[target_coord]
    return res




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rotate a given image')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('angle', type=int, help='angle : positive = counterclockwise')
    args = parser.parse_args()
    filename = args.filename
    angle = args.angle

    outputfile = os.path.splitext(filename)[0] + '_rot.png'
    im = mpimg.imread(filename)
    rotated = rotate(im, angle)
    mpimg.imsave(outputfile, rotated)

