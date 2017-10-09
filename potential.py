from ioutils import read_strings
from charge import Charge
import re
import matplotlib.image as mpimg
import numpy as np

def total_potential(coord, charges):
    res = 0
    for charge in charges:
        res += charge.potential_at(coord)
    return res

def color_for(potential):
    # res= 0.5+(potential/2.0e10/255)
    res= 0.5+(potential/2.0e10/255)
    if res < 0:
        return 0
    if res > 1:
        return 1
    return res

def create_image(charges):
    SIZE=100
    potentials = np.zeros((SIZE,SIZE,3))
    for x in range(SIZE):
        for y in range(SIZE):
            coord = (x/SIZE, y/SIZE)
            pot = total_potential(coord, charges)
            potentials[SIZE-y-1,x]= color_for(pot)

    mpimg.imsave('potentials.png', potentials)


if __name__ == "__main__":
    content = read_strings()
    charges =[]
    for line in content:
        values = re.split('\s+', line)
        if len(values) == 3:
            values = [float(x) for x in values]
            coord = tuple(values[0:2])
            q = values[2]
            charges += [Charge(coord,q)]
    print(charges)
    create_image(charges)




