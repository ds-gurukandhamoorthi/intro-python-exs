import argparse
import math
from taylor_series import taylor_series, step_phi
import scipy.stats 

TOLERANCE = 10**-10
def binary_search_interval(lo, hi, cmp_func, func, y):
    midpoint = (lo + hi) / 2
    res_comp = cmp_func(func, midpoint, TOLERANCE, y)
    if res_comp == 0:
        return midpoint
    if res_comp > 0:
        return binary_search_interval(midpoint, hi, cmp_func, func, y)
    return binary_search_interval(lo, midpoint, cmp_func, func, y)

def cmp_func(func, x0, tolerance, est):
    "Tells if a given function evaluates to ext at x0 with the given tolerance: f(x0) = est ? Is the estimate greater than the actual value?"
    val = func(x0)
    if abs(val-est) < tolerance:
        return 0
    if est > val:
        return 1
    return -1





def phi(x):
    return  (1/math.sqrt(2*math.pi)) * math.exp(-.5*x**2)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x-mu)/sigma)/sigma

def Phi(x):
    return 0.5 + phi(x) * taylor_series(x, x, step_phi)

def cdf(x, mu=0.0, sigma=1.0):
    return Phi((x-mu)/sigma)

def inverse(func, y,  lo, hi, cmp_func):
    return binary_search_interval(lo, hi, cmp_func, func, y)

def Phi_inverse(y):
    return inverse(Phi, y, -8.0, 8.0, cmp_func)





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
    print(z, y, x)


