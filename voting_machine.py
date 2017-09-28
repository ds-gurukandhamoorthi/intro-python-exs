import argparse
from numpy.random import choice


def vote(percentage):
    return choice(range(0,len(percentage)), size=1, p= percentage)[0]

def erroneous(candidate):
    if candidate == 0:
        return 1
    elif candidate == 1:
        return 0


if __name__ == "__main__":
    CANDIDATES = ['A','B']
    PERCENTAGE = [0.51, 0.49]

    parser = argparse.ArgumentParser(description='Simulate election')
    parser.add_argument('nb_voters', type=int, help='number of voters')
    parser.add_argument('perct_error', type=int, help='percentage of error : ex: 5')
    args = parser.parse_args()
    nb_voters = args.nb_voters
    nb_errors = nb_voters * args.perct_error/100

    votes = [0] * len(CANDIDATES)
    for i in range(nb_voters):
        who = vote(PERCENTAGE)
        if i < nb_errors:
            votes[erroneous(who)] += 1
        else:
            votes[who] += 1
    print(CANDIDATES)
    print(votes)
            





