import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from math import cos, sin, radians, pi
from geomutils import is_valid_coord, lc_to_xy, xy_to_lc
from distance import euclideanDist



def waved_coord_cartesian(source, amplitude, frequency):
    "waved coordinate source with the given amplitude and frequency"
    target_x = int(source[0])
    target_y = int(source[1] + amplitude * sin(2*pi*source[0]/frequency))
    return target_x, target_y

def waved(source, amplitude, frequency, height):
    "waved coordinate source with the given amplitude and frequency: in a row first... matrix coord"
    source_ = lc_to_xy(source, height)
    target_ = waved_coord_cartesian(source_, amplitude, frequency)
    target = xy_to_lc(target_, height)
    return target



def wave(img_array, amplitude, frequency):
    shp = img_array.shape
    res = np.zeros(shp)
    for i, row in enumerate(res):
        for j, _ in enumerate(row):
            target_coord = waved((i,j), amplitude, frequency, shp[0])
            # target_coord = waved_coord_cartesian((i,j), amplitude, frequency)
            if is_valid_coord(target_coord, shp[0:2]):
                res[i,j] = img_array[target_coord]
    return res




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wave transform a given image')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('amplitude', type=float, help='amplitude of the wave')
    parser.add_argument('frequency',type=float,  help='frequency of the wave')
    args = parser.parse_args()
    filename = args.filename
    amplitude = args.amplitude
    frequency = args.frequency

    outputfile = os.path.splitext(filename)[0] + '_wave.png'
    im = mpimg.imread(filename)
    wvd = wave(im,amplitude, frequency)
    mpimg.imsave(outputfile, wvd)

