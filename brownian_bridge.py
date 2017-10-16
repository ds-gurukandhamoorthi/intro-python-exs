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
        m = m[0], m[1] +rand_height
        points += brownian_bridge(frm, m,  variance/scale, scale)
        points += brownian_bridge(m, to,  variance/scale, scale)
    return points

def brownian_island(frm, to, variance, scale, n):
    if n == 0:
        return [(frm, to)]
    m = midpoint(frm,to)
    rand_height = normal(0,sqrt(variance))
    rand_width = normal(0,sqrt(variance))
    m = m[0] + rand_width, m[1] +rand_height
    points = []
    points += brownian_island(frm, m,  variance/scale, scale, n-1)
    points += brownian_island(m, to,  variance/scale, scale, n-1)
    return points

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a brownian bridge or island')
    parser.add_argument('hurst_exponent', type=float, help='Hurst exponent : controls smoothness')
    parser.add_argument('--volatility', type=float, help='volatility as variance')

    args = parser.parse_args()
    hurst_exponent = args.hurst_exponent
    if args.volatility:
        volatility = args.volatility
    else:
        volatility = 0.01

    scale = 2**(2*hurst_exponent)
    # scale = 2.7
    # ps = brownian_bridge((0,1/2),(1,1/2), volatility, scale)
    ps = brownian_island((1/2,1/2),(1/2,1/2), volatility, scale, 10)  #Enter volatility 0.75 from commandline

    lc = matplotlib.collections.LineCollection(ps)
    fig, ax = plt.subplots(1,1)
    ax.axis('equal')
    ax.add_collection(lc)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_title('Brownian bridge')
    plt.show()
