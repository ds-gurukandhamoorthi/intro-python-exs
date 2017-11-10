import random
import sys
import operator
from collections import Counter


def trial(nbTimes):
    stat = Counter()
    deck = list(range(52))
    for i in range(nbTimes):
        shuffled = random.sample(deck, len(deck))
        typeHand = nbCardsPerSuit(shuffled[:13])
        stat[typeHand] += 1
        typeHand = nbCardsPerSuit(shuffled[13:26])
        stat[typeHand] += 1
        typeHand = nbCardsPerSuit(shuffled[26:39])
        stat[typeHand] += 1
        typeHand = nbCardsPerSuit(shuffled[39:52])
        stat[typeHand] += 1
    return stat


def nbCardsPerSuit(hand):
    res = [0, 0, 0, 0]
    for val in hand:
        res[val % 4] += 1
    return tuple(sorted(res, reverse=True))


if __name__ == "__main__":
    n = int(sys.argv[1])
    res = trial(n)
    print(sorted(res.items(), key=operator.itemgetter(1), reverse=True))
