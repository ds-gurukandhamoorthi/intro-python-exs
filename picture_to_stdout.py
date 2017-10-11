import matplotlib.image as mpimg
import numpy as np
import argparse

def to_255(color01):
    "Converts a color defined in 0-1 to 0-255"
    return tuple(int(x*255) for x in color01)

def to_stdout(filename):
    im = mpimg.imread(filename)
    height,width = im.shape[0:2]
    print(width, height)
    for row in im:
        for pxl in row:
            print(to_255(pxl), end='')
        print('')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Output an image file as triplets into stdout')
    parser.add_argument('filename',  help='name of the image file')
    args = parser.parse_args()
    filename = args.filename
    to_stdout(filename)
