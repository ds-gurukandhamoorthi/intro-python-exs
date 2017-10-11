import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from functools import partial


def tile(img_array, horiz_repeat, vertic_repeat):
    return np.tile(img_array, (vertic_repeat, horiz_repeat, 1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tile a given image')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('horiz_repeat', type=int, help='number of horizontal tiles')
    parser.add_argument('vertic_repeat', type=int, help='number of vertical tiles')
    args = parser.parse_args()
    filename = args.filename
    horiz_repeat = args.horiz_repeat
    vertic_repeat = args.vertic_repeat

    outputfile = os.path.splitext(filename)[0] + str(horiz_repeat) +'x' +str(vertic_repeat) + '.png'
    im = mpimg.imread(filename)
    tiled = tile(im, horiz_repeat, vertic_repeat)
    print(im.shape, tiled.shape)
    print(tiled)
    mpimg.imsave(outputfile, tiled)

