import numpy as np
import matplotlib.image as mpimg
import argparse

def mandelbrot_set(n, start):
    z0 = start
    if n == 0:
        return z0
    z = z0
    for i in range(n):
        z = z * z + z0
    return z

def how_long_within(start, nb_max_iter):
    z0 = start
    z = z0
    for i in range(nb_max_iter):
        if abs(z) > 2:
            return i
        z = z * z + z0
    return nb_max_iter

MAX=255
def mandelbrot_image_matrix(nb_pxls, start, radius):
    mtrx = np.zeros((nb_pxls,nb_pxls,3))
    for i, row in enumerate(mtrx):
        for j, pxl in enumerate(row):
            x0 = start.real -(radius/2) +(j*radius/nb_pxls)
            y0 = start.imag -(radius/2) +(i*radius/nb_pxls)
            z0 = complex(x0, y0)
            # if how_long_within(z0, MAX) > 100:
            #     print(z0, ' > 100 iters')
            gray = (MAX - how_long_within(z0, MAX))/MAX
            color = (gray, gray, gray)
            mtrx[i,j] = color
    return mtrx

            
            # mtrx[i,j] = 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw mandelbrot set')
    parser.add_argument('nb_pixels', type=int, help='size in pixels of the square image')
    parser.add_argument('xc', type=float, help='real part of the start')
    parser.add_argument('yc', type=float, help='imaginary part of the start')
    parser.add_argument('radius', type=float, help='enter smaller numbers to zoom near')
    args = parser.parse_args()
    nb_pixels = args.nb_pixels
    xc = args.xc
    yc = args.yc 
    radius = args.radius
    res = mandelbrot_image_matrix(nb_pixels, complex(xc,yc),radius) 
    mpimg.imsave('tes.png', res)
        

