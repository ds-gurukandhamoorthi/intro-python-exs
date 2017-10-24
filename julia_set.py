import argparse
import random
import numpy as np
import matplotlib.image as mpimg


def how_long_within(z, center, nb_max_iter):
    z_ = z
    for i in range(nb_max_iter):
        if abs(z_) > 2:
            return i
        z_ = z_ * z_ + center
    return nb_max_iter


XMIN, XMAX = -2, 2
YMIN, YMAX = -2, 2
XWIDTH, YWIDTH = XMAX - XMIN, YMAX - YMIN


MAX = 255
COLORS = [(random.random(), random.random(), random.random())
          for i in range(MAX + 1)]


def julia_image_matrix(nb_pxls, center):
    mtrx = np.zeros((nb_pxls, nb_pxls, 3))
    z0 = center
    for i, row in enumerate(mtrx):
        for j, pxl in enumerate(row):
            z = complex(j / nb_pxls * XWIDTH + XMIN,
                        i / nb_pxls * YWIDTH + YMIN)
            # gray = (MAX - how_long_within(z0, MAX))/MAX
            # color = (gray, gray, gray)
            index = MAX - how_long_within(z, z0, MAX)
            color = COLORS[index]
            mtrx[i, j] = color
    return mtrx


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw julia set')
    parser.add_argument('nb_pixels', type=int,
                        help='size in pixels of the square image')
    parser.add_argument('a', type=float, help='real part of the start')
    parser.add_argument('b', type=float, help='imaginary part of the start')
    args = parser.parse_args()
    nb_pixels = args.nb_pixels
    a = args.a
    b = args.b
    res = julia_image_matrix(nb_pixels, complex(a, b))
    mpimg.imsave('tes.png', res)
