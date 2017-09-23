import argparse
from math import cos, sin, asin, radians,sqrt, degrees


def haversine(d1,a1, d2,a2):
    def haver(angle):
        return sin(angle/2)**2
    d = d2 - d1
    a = a2 - a1
    h = haver(d) + cos(d1)*cos(d2)*haver(a)
    return 2*asin(sqrt(h))



parser = argparse.ArgumentParser(description='calculate the angle between two stars using the haversine formula')

parser.add_argument('d1', type=float, help='declination of the first star')
parser.add_argument('a1', type=float, help='right ascension for the first star')
parser.add_argument('d2', type=float, help='declination of the second star')
parser.add_argument('a2', type=float, help='right ascension for the second star')

args = parser.parse_args()
d1 = radians(args.d1)
a1 = radians(args.a1)
d2 = radians(args.d2)
a2 = radians(args.a2)
print(degrees(haversine(d1,a1, d2,a2)))





