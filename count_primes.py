import argparse
from int_utils import count_primes

parser = argparse.ArgumentParser(description='Prints the number of primes below the given number')
parser.add_argument('n', type=int, help='the number until which primes should be counted')
args = parser.parse_args()
n = args.n





print(count_primes(n))
