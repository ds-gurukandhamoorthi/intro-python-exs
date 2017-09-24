import sys
from math import log, exp, sqrt
from gauss import cdf

def log_factorial(n):
    return sum(log(i) for i in range(1,n+1))

def binomial_dist(n, k, p):
    ln_f = k * log(p) + (n-k) * log(1-p) + log_factorial(n) - log_factorial(k) - log_factorial(n-k)
    return exp(ln_f)

#FIXME : the following code is not verified
def binomial_dist_approx(n, k, p):
    return cdf(k+0.5, n*p, (n*p*sqrt(1-p))) - cdf(k-0.5, n*p, n*p*sqrt(1-p)) 



if __name__ == "__main__":
    print(binomial_dist(3, 3, 0.5))

    n = int(sys.argv[1])
    p = float(sys.argv[2])

    dist = [binomial_dist(n,k,p) for k in range(0,n+1)]
    print(dist)
    print(sum(dist))

    dist = [binomial_dist_approx(n,k,p) for k in range(0,n+1)]
    print(dist)
    print(sum(dist))

    


