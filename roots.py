import argparse
from math import sqrt
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Roots of a polynomial a×X²+bX+c ')
    parser.add_argument('a', type=float, help='a')
    parser.add_argument('b', type=float, help='b')
    parser.add_argument('c', type=float, help='c')
    args = parser.parse_args()
    a = args.a
    b = args.b
    c = args.c
    discrim = b**2 - 4*a*c
    if discrim > 0:
        print((-b + sqrt(discrim))/(2*a),(-b - sqrt(discrim))/(2*a))
    elif discrim == 0:
        print((-b + sqrt(discrim))/(2*a))
    else:
        print(complex(-b/2*a, sqrt(-discrim)/(2*a)),complex(-b/2*a, -sqrt(-discrim)/(2*a)))
