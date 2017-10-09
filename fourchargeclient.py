import argparse
from geomutils import neighbours
from charge import Charge
from potential import total_potential

def get_neighs(coord, width):
    POINTS=((0,width),(0,-width),(width,0),(-width,0))
    return neighbours(coord, POINTS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Four charges in the cardinal direction')
    parser.add_argument('w', type=float, help='distance from center')
    args = parser.parse_args()
    w  = args.w 
    CENTER = (0.5,0.5)
    CHARGE = 1.0
    charges =[]
    for coord in get_neighs(CENTER, w):
        charges += [Charge(coord, CHARGE)]

    point_of_interest = (.25,.5)
    print('%.2e' % total_potential(point_of_interest, charges))
    print( total_potential(point_of_interest, charges))




