import sys, math
import argparse

parser = argparse.ArgumentParser(description='Continously compounded interest')
parser.add_argument('amount', type=float, help='inital amount invested')
parser.add_argument('roi', type=float, help=r'rate of interest as percent (ex: 5 for 5%%)')
parser.add_argument('years', type=int, help='number of years')
args = parser.parse_args()
amount = args.amount
roi = args.roi / 100
years = args.years

res = amount * math.e ** (roi * years)
print(res)
