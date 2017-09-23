import argparse

def are_triangular(a,b,c):
    a_, b_, c_ = sorted((a,b,c))
    return c_ < a_ + b_


parser = argparse.ArgumentParser(description='Say if the three lengths can make a triangle')
parser.add_argument('a', type=float, help='length of a triangle')
parser.add_argument('b', type=float, help='length of a triangle')
parser.add_argument('c', type=float, help='length of a triangle')

args = parser.parse_args()

a = args.a
b = args.b
c = args.c


print(are_triangular(a,b,c))
