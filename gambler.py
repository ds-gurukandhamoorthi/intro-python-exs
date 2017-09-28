import argparse
import sys
import random

def gambler_ruin_single_trial(amount_risked, goal, prob_winning, max_bets):
    bets = 0
    amount = amount_risked
    while 0 < amount < goal and bets <= max_bets:
        amount += 1 if random.random() <= prob_winning else 0
        bets += 1
    return (amount, bets)

def gambler_ruin(amount_risked, goal, prob_winning, max_bets, nb_trials):
    wins = 0
    total_bets = 0
    gains = 0
    for i in range(nb_trials):
        amount, bets = gambler_ruin_single_trial(amount_risked, goal, prob_winning, max_bets)
        if amount >= goal:
            wins += 1
        total_bets += bets
        gains += amount
    return (gains, wins, total_bets,nb_trials, wins/nb_trials)
        

def probability(p):
    prob = float(p)
    if not 0<=prob<=1:
        msg = "probability must be between 0 and 1"
        raise argparse.ArgumentTypeError(msg)
    return prob

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulation for a gambler')
    parser.add_argument('initial', type=int, help='initial amount gambled')
    parser.add_argument('goal', type=int, help='goal amount at which gambling is stopped')
    parser.add_argument('prob', type=probability, help='prob of winning')
    parser.add_argument('max_bets', type=int, help='maximum number of bets placed')
    parser.add_argument('trials', type=int, help='number of times the experiment should be carried on')
    args = parser.parse_args()
    initial = args.initial
    goal = args.goal
    trials = args.trials
    prob = args.prob
    max_bets = args.max_bets

    print(gambler_ruin(initial, goal, prob, max_bets, trials))
        
