import argparse
import math
from taylor_series import taylor_series, step_phi
import scipy.stats 
from binary_search_function import inverse 
from pynverse import inversefunc

TOLERANCE = 10**-5


def phi(x):
    return  (1/math.sqrt(2*math.pi)) * math.exp(-.5*x**2)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x-mu)/sigma)/sigma

def Phi(x):
    return 0.5 + phi(x) * taylor_series(x, x, step_phi)

def cdf(x, mu=0.0, sigma=1.0):
    return Phi((x-mu)/sigma)

def Phi_inverse(y):
    return inverse(Phi, y, -8.0, 8.0)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate cumulative Gaussian distribution')
    parser.add_argument('z', type=float, help='point at which to calculate the function')
    parser.add_argument('mu',metavar='μ', type=float, help='mu : average')
    parser.add_argument('sigma',metavar='σ', type=float, help='sigma : std deviation ')
    args = parser.parse_args()
    z = args.z
    mu = args.mu
    sigma = args.sigma
    print(cdf(z, mu, sigma), scipy.stats.norm(mu, sigma).cdf(z))

    
    print(pdf(z, mu, sigma), scipy.stats.norm(mu, sigma).pdf(z))
    y = Phi(z)
    x = Phi_inverse(y)
    print(z, y, x, inversefunc(Phi,y_values=y, domain=[-8,8], accuracy=25))


