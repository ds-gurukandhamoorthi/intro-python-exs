from Complex import Complex
import numpy as np
import matplotlib.image as mpimg

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

def mandelbrot_image_matrix(n, start):
    mtrx = np.zeros((n,n))
    for i, row in mtrx:
        for j, pxl in row:
            mtrx[i,j] = 

if __name__ == "__main__":
    z0 = Complex(-.633,-.01)
    print(how_long_within(z0,600))
        

