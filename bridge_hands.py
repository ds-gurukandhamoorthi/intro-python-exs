import random
import sys
import operator


def trial(nbTimes):
    stat={}
    deck = list(range(52))
    for i in range(nbTimes):
        shuffled = random.sample(deck,len(deck))
        typeHand =nbCardsPerSuit(shuffled[:13])
        stat[typeHand] = stat.get(typeHand,0) + 1
        typeHand =nbCardsPerSuit(shuffled[13:26])
        stat[typeHand] = stat.get(typeHand,0) + 1
        typeHand =nbCardsPerSuit(shuffled[26:39])
        stat[typeHand] = stat.get(typeHand,0) + 1
        typeHand =nbCardsPerSuit(shuffled[39:52])
        stat[typeHand] = stat.get(typeHand,0) + 1
    return stat

def nbCardsPerSuit(hand):
    res = [0,0,0,0]
    for val in hand:
        res[val%4] += 1
    return tuple(sorted(res,reverse=True))

if __name__ == "__main__":
    n = int(sys.argv[1])
    res=trial(n)
    print(sorted(res.items(), key=operator.itemgetter(1), reverse=True))
