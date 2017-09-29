from geomutils import midpoint
from math import sqrt
from numpy.random import normal
import matplotlib.pyplot as plt
import matplotlib.collections
import argparse

TOLERANCE = 0.01 #epsilon

def brownian_bridge(frm, to, variance, scale):
    points = []
    if abs(to[0] - frm[0]) < TOLERANCE:
        points += [(frm ,to)]
    else:
        m = midpoint(frm,to)
        rand_height = normal(0,sqrt(variance))
        print("rand_height", rand_height)
        m = m[0], m[1] +rand_height
        points += brownian_bridge(frm, m,  variance/scale, scale)
        points += brownian_bridge(m, to,  variance/scale, scale)
    return points

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a brownian bridge')
    parser.add_argument('hurst_exponent', type=float, help='Hurst exponent : controls smoothness')
    parser.add_argument('--volatility', type=float, help='volatility as variance')

    args = parser.parse_args()
    hurst_exponent = args.hurst_exponent
    if args.volatility:
        volatility = args.volatility
    else:
        volatility = 0.01

    scale = 2**(2*hurst_exponent)
    ps = brownian_bridge((0,1/2),(1,1/2), volatility, scale)

    lc = matplotlib.collections.LineCollection(ps)
    fig, ax = plt.subplots(1,1)
    ax.add_collection(lc,autolim=True)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_title('Brownian bridge')
    plt.show()
