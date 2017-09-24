import argparse
from taylor_series import stepExp, taylor_series_coeffs
import math

#[a0,a1,a2,a3] a0 + a1 *x  + a2 *x2 + a3 * x3
def horner(polynome_array, x):
    total = 0
    for coeff in reversed(polynome_array):
        total = total * x + coeff
    return total

def horner_rec(polynome_array, x):
    if len(polynome_array) == 1:
        return polynome_array[0]
    return polynome_array[0] + x * horner_rec(polynome_array[1:],x)


def exponential(x, n):
    "Using Taylor and Horner"
    tylr_series = taylor_series_coeffs(1, n, stepExp)
    return horner(tylr_series, x)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate exponential using Horner''s method')
    parser.add_argument('nums', metavar='N', type=float, nargs='+', help='numbers for which exponential must be calculated')
    parser.add_argument('--nb-steps', type=int, help='number of steps : default 30', default=30)
    args = parser.parse_args()
    nums = args.nums



    
    NBSTEPS = args.nb_steps
    for x in nums:
        print(exponential(x,NBSTEPS))
        print(math.exp(x))
        print('')

