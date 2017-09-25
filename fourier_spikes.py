import argparse
import numpy
from math import cos
import matplotlib.pyplot as plt


def fourier_spike(t,n):
    "Returns the average of the n terms of a cosinus series"
    series = (cos(i*t) for i in range(1,n+1))
    return sum(serie)/n

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draws Fourier spikes')
    parser.add_argument('n', type=int, help='n')
    args = parser.parse_args()
    n = args.n

    FROM = -10
    TO = 10
    NB_INTERV = 500
    xs = numpy.linspace(FROM, TO, NB_INTERV)
    ys = [fourier_spike(x,n) for x in xs]
    print(xs,ys)
    plt.plot(xs,ys)
    plt.show()

