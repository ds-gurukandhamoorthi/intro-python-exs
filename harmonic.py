import argparse
import sys
import math
import mpmath

# harmonicSum = 1

# for i in range(2, n+1):
#     harmonicSum += 1/i

# print(harmonicSum)

def harmonic_sum_small(n):
    harmsum = [0.0]*(n+1)
    for i in range(1,n+1):
        harmsum[i]=harmsum[i-1] + 1/i
    return harmsum[n]

def harmonic_sum_large(n):
    # euler_mascheroni_constant = 0.577215664901532
    euler_mascheroni_constant = mpmath.euler
    return math.log(n) + euler_mascheroni_constant + 1/(2*n) - 1/(12*n*n) + 1/(120*n**4)

def harmonic(n):
    if n < 100:
        return harmonic_sum_small(n)
    return harmonic_sum_large(n)

def harmonic_rec(n):
    if n == 1:
        return 1
    return harmonic_rec(n-1) + 1/n

def harmonic_iter(n):
    tot = 1
    for i in range(2, n+1):
        tot += 1/i
    return tot

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the nth harmonic number')
    parser.add_argument('nums', metavar='N', nargs='+', type=int, help='index of the needed harmonic number')
    args = parser.parse_args()
    nums = args.nums
    for n in nums:
        print(harmonic(n))
        print(harmonic_sum_small(n))
        print(harmonic_sum_large(n))


