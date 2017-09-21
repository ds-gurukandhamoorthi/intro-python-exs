import argparse
import sys
import random

parser = argparse.ArgumentParser(description='Simulation for a gambler')
parser.add_argument('initial', type=int, help='initial amount gambled')
parser.add_argument('goal', type=int, help='goal amount at which gambling is stopped')
parser.add_argument('trials', type=int, help='number of times the experiment should be carried on')
parser.add_argument('prob', type=float, help='prob of winning')
parser.add_argument('max_bets', type=int, help='maximum number of bets placed')
args = parser.parse_args()
initial = args.initial
goal = args.goal
trials = args.trials
prob = args.prob
max_bets = args.max_bets

amount = initial

wins = 0
bets = 0
i = 0
while i <= trials:
    amount = initial
    this_bets = 0
    while 0 < amount < goal and this_bets <= max_bets:
        if random.random() <= prob:
            amount += 1
        else:
            amount -= 1
        bets += 1
        this_bets += 1
        print("*" * amount)
    if amount >=goal:
        wins += 1
    i+=1
    print('')

print(wins/trials)
print(bets//trials)
    
