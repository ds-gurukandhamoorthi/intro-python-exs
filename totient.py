from int_utils import totatives, totient
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Euler''s totient : number of integers less than n and relatively prime with n')
    parser.add_argument('n', type=int, help='integer n')
    args = parser.parse_args()
    n=args.n
    print(totient(n))
    print(list(totatives(n)))


