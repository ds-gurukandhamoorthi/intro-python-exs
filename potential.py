from ioutils import read_strings
from charge import Charge
import re
import matplotlib.image as mpimg
import numpy as np
import random
from itertools import product

def total_potential(coord, charges):
    res = 0
    for charge in charges:
        res += charge.potential_at(coord)
    return res


def color_for(potential):
    res= 0.5+(potential/2.0e10/255)
    if res < 0:
        return 1
    if res > 1:
        return 0
    if int(res*255) % 5 == 0:
        return 0
    return 1

def color_for_(potential):
    # res= 0.5+(potential/2.0e10/255)
    res= 0.5+(potential/2.0e10/255)
    if res < 0:
        return 0
    if res > 1:
        return 1
    return res

def create_image(charges, filename):
    SIZE=100
    potentials = np.zeros((SIZE,SIZE,3))
    for x in range(SIZE):
        for y in range(SIZE):
            coord = (x/SIZE, y/SIZE)
            pot = total_potential(coord, charges)
            potentials[SIZE-y-1,x]= color_for(pot)

    mpimg.imsave(filename, potentials)

def random_Charge(mean, sd):
    x,y = random.random(), random.random()
    charge = np.random.normal(mean, sd)
    return Charge((x,y), charge)

def minimum_potential_point(charges):
    NB_SPLIT=100
    values = np.linspace(0,1,NB_SPLIT+1)
    coords = product(values,values)
    minim = None
    res = None
    for coord in coords:
        pot = total_potential(coord, charges)
        if minim is None:
            minim = pot
        elif pot < minim:
            minim = pot
            res = Charge(coord, pot)
    return res




if __name__ == "__main__":
    # content = read_strings()
    # charges =[]
    # for line in content:
    #     values = re.split('\s+', line)
    #     if len(values) == 3:
    #         values = [float(x) for x in values]
    #         coord = tuple(values[0:2])
    #         q = values[2]
    #         charges += [Charge(coord,q)]
    n = 5
    charges = [random_Charge(10,10) for i in range(n)]
    for c in charges:
        print(c)
    create_image(charges, 'potentials.png')
    charges = [random_Charge(20,1) for i in range(2)]
    for c in charges:
        print(c)
    print(minimum_potential_point(charges))


    #mutable charges exercise
    n = 10
    a = [None] * 3
    a[0] = Charge((.4, .6), 50)
    a[1] = Charge((.5, .5), -5)
    a[2] = Charge((.6, .6), 50)
    for i in range(100):
        create_image(a, 'mutab_charge'+str(i)+'.png')
        a[1] += (-2.0)







