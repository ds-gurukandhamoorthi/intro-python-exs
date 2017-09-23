import argparse
from gauss import Phi
from math import log, sqrt,exp

def black_scholes(s, x, r, sigma, t):
    a = (log(s/x) + (r + 0.5*sigma**2) *t) / (sigma * sqrt(t))
    b = a - sigma* sqrt(t)
    return s* Phi(a) - x * exp(-r*t) * Phi(b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calcualte the Black-Scholes values')
    parser.add_argument('s', type=float, help='current stock price')
    parser.add_argument('x', type=float, help='exercise price')
    parser.add_argument('r', type=float, help='risk-free interest rate')
    parser.add_argument('sigma', metavar='σ', type=float, help='standard deviation of the stock''s return (volatility)')
    parser.add_argument('t', type=float, help='time to maturity (in years)')
    args = parser.parse_args()
    s = args.s
    x = args.x
    r = args.r
    sigma = args.sigma
    t = args.t
    print(black_scholes(s, x, r, sigma, t))
    
