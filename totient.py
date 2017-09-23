from gcd import gcd
import argparse

def is_relataively_prime(a, b):
    return gcd(a,b) == 1


def totatives(n):
    return [i  for i in range(1,n+1) if is_relataively_prime(i,n)]

def totient(n):
    "Euler's totient : number of integers less than n and relatively prime with n"
    return len(totatives(n))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Euler''s totient : number of integers less than n and relatively prime with n')
    parser.add_argument('n', type=int, help='integer n')
    args = parser.parse_args()
    n=args.n
    print(totient(n))
    print(list(totatives(n)))


