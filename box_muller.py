import argparse
import sys, math
import random
sys.path.append('../')
import stddraw
import matplotlib.pyplot as plt

def histogram(start, end, subdivisions, array):
    res = [0] * subdivisions
    for val in array:
        i = which_subdivision(start, end, subdivisions, val)
        if i is not None:
            res[i] += 1
    return res

def which_subdivision(start, end, subdivisions, val):
    "Given [start, end] and n subdivisions tells in which subdivision the val falls"
    if start <= val <= end:
        interval_len = (end - start) / subdivisions
        return int((val-start)/interval_len)
    return None

def gaussian_box_muller():
    u = random.random()
    v = random.random()

    z = math.sin(2*math.pi*v)*(-2*math.log(u))**0.5
    return z

def gaussian():
    r = 0.0
    while (r >= 1) or (r == 0.0):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) /r)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculates gaussian using box muller')
    parser.add_argument('nb_trials', type=int, help='number of time the calculation must be carried out')
    parser.add_argument('--histogram', help='help for ', action='store_true')
    args = parser.parse_args()
    nb_trials = args.nb_trials

    values = [gaussian_box_muller() for i in range(nb_trials)]
    mi = -1
    ma = 1
    subdiv = 20
    h=histogram(mi,ma,subdiv,values)
    interv = (ma - mi) /subdiv
    xs = [ mi + i * interv for i in range(0,subdiv)]
    print(xs)
    print(h)
    if args.histogram:
        plt.plot(xs,h)
        plt.ylabel('frequency')
        plt.xlabel('gaussian')
        plt.show()
