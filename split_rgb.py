import matplotlib.image as mpimg
import numpy as np
import argparse
import os

def split_rgb(filename):
    prefix = os.path.splitext(filename)[0]
    im = mpimg.imread(filename)
    r = lambda r, g, b: tuple((r,0,0))
    g = lambda r, g, b: tuple((0,g,0))
    b = lambda r, g, b: tuple((0,0,b))
    shape = im.shape
    red = np.zeros(shape)
    green = np.zeros(shape)
    blue = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            red[i][j] = r(*im[i][j])
            green[i][j] = g(*im[i][j])
            blue[i][j] = b(*im[i][j])
    mpimg.imsave(prefix+'_r.png', red)
    mpimg.imsave(prefix+'_g.png', green)
    mpimg.imsave(prefix+'_b.png', blue)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Flip an image')
    parser.add_argument('filename',  help='name of the image file to flip')
    args = parser.parse_args()
    filename = args.filename
    split_rgb(filename)
