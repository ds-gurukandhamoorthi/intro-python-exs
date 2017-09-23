import argparse
import math

def sigmoid(x):
    return 1/(1+math.exp(-x))
parser = argparse.ArgumentParser(description='Calculate the sigmoid function')
parser.add_argument('x', type=float, help='point at which to calculate the function')
args = parser.parse_args()
x = args.x

print(sigmoid(x))

