import matplotlib.image as mpimg
import numpy as np
import argparse
import os

def flip_image(filename):
    prefix = os.path.splitext(filename)[0]
    im = mpimg.imread(filename)
    flipped = np.flipud(im)
    mpimg.imsave(prefix+'_flipud.png', flipped)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Flip an image')
    parser.add_argument('filename',  help='name of the image file to flip')
    args = parser.parse_args()
    filename = args.filename
    flip_image(filename)
