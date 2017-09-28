import argparse
from diceSimulation import die

def sum_two_dice(prb_dist=None):
    return die(prb_dist) + die(prb_dist)


def crap_game(prb_dist=None):
    s = sum_two_dice(prb_dist)
    if s in {7,11}:
        return True
    if s in {2, 3, 12}:
        return False
    while True:
        nxt = sum_two_dice()
        if nxt == s:
            return True
        if nxt == 7:
            return False

def loaded_dice_prob(p):
    prob = [(1-1/6)/4] * 6
    prob[0] = p
    prob[5] = (1/6)-p
    return prob

def prob_one_face(p):
    prob = float(p)
    if not 0<=prob<=1/6:
        msg = "probability of a face must be between 0 and 1/6"
        raise argparse.ArgumentTypeError(msg)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate crap game')
    parser.add_argument('nb_trials', type=int, help='number of times the experiment must be carried out')
    parser.add_argument('--prob_1', type=prob_one_face, help='probability of 1 (between 0 and 1/6)')
    args = parser.parse_args()
    nb_trials = args.nb_trials
    prob_1 = args.prob_1
    # print(loaded_dice_prob(0.1))
    # print(sum(loaded_dice_prob(0.1)))
    if args.prob_1:
        wins=sum([crap_game(loaded_dice_prob(prob_1)) for i in range(nb_trials)])
    else:
        wins=sum([crap_game() for i in range(nb_trials)])
    print(wins, nb_trials)
