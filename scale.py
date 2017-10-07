from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from functools import partial

WEIGHTED_RGB = [0.299, 0.587, 0.114]

def scale(orig_geom, new_geom, coord):
    return tuple([ int((x/n)*o) for x,n,o in zip(coord, new_geom, orig_geom)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to grayscale')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('width', type=int, help='width of the image')
    parser.add_argument('height', type=int, help='height of the image')
    parser.add_argument('--output',  help='output file name', action='store_true')
    args = parser.parse_args()
    filename = args.filename
    width = args.width
    height = args.height
    if args.output is False:
        fn, ext = os.path.splitext(filename)
        outputfile = fn+'_scaled.png'
    else:
        outputfile = args.output


    #method2
    im2 = mpimg.imread(filename)
    scaled = np.zeros([height, width, 3])
    orig_geom = im2.shape[:2]
    new_geom=(height, width)
    scl = partial(scale, orig_geom, new_geom)
    for i, row in enumerate(scaled):
        for j, pixel in enumerate(row):
            scaled[i,j] = im2[scl((i,j))]


    # print(im2)
    # gray = np.dot(im2[...,:3], WEIGHTED_RGB)
    plt.imshow(scaled)
    plt.show()
    mpimg.imsave(outputfile, scaled)

