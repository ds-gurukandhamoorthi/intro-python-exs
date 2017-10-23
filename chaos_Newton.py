import numpy as np
import matplotlib.image as mpimg

def f(z):
    return z**4 -1

def f_(z):
    return 4*z**3

def iter_apply(funct, deriv, start, n):
    res = start
    for i in range(n):
        if deriv(res) == 0:
            return None
        res = res - funct(res)/deriv(res)
    return res

def color_for(comp_num):
    nbs = [1, -1, 1j, -1j]
    colors = [(0,0,1), (0,1,0),(1,0,0), (1,1,1)]
    if comp_num is None:
        return (0,0,0)
    for i, c in enumerate(nbs):
        if abs(c-comp_num) < 10**-3:
            return colors[i]
    return (0,0,0)

def Newton(nb_pixels, radius=1):
    image = np.zeros((nb_pixels, nb_pixels, 3))
    for i,x in enumerate(np.linspace(-radius, radius, nb_pixels)):
        for j,y in enumerate(np.linspace(-radius, radius, nb_pixels)):
            val = iter_apply(f, f_, complex(x,y), 100)
            image[nb_pixels-1-i,j] = color_for(val)
    return image

if __name__ == "__main__":
    img = Newton(512, radius=1)
    mpimg.imsave('tes.png', img)






