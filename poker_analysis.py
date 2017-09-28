from cards import get_hand
from rle import rle

RANKS = list(range(0,13))
SUITS = ['C','D','H','S']

def get_deck_tuple():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = (suit, rank)
            deck += [card]
    return deck

def rle_suit(hand):
    suits = get_suits(hand)
    return sorted(rle(sorted(suits)),reverse=True)

def rle_rank(hand):
    ranks = get_ranks(hand)
    return sorted(rle(sorted(ranks)),reverse=True)


def get_suits(hand):
    return [suit for suit, r in hand]

def get_ranks(hand):
    return [rank for s, rank in hand]

def get_counts(rle):
    return [count for count, el in rle]

def get_pattern_ranks(hand):
    return get_counts(rle_rank(hand))


def recognize(hand):
    ranks_ptrn = get_pattern_ranks(hand)
    if ranks_ptrn == [5]:
        return "flush"
    if ranks_ptrn == [3, 2]:
        return "full house"
    if ranks_ptrn == [4, 1, 1]:
        return "four of a kind"
    if ranks_ptrn == [3, 1, 1]:
        return "three of a kind"
    if ranks_ptrn == [2, 2, 1]:
        return "two pair"
    if ranks_ptrn == [2, 1, 1, 1]:
        return "one pair"
    return "not recognized"




if __name__ == "__main__":
    h=get_hand(get_deck_tuple())
    print(h)
    print(get_suits(h))
    print(rle_suit(h))
    print(get_ranks(h))
    rs = (rle_suit(h))
    rr = (rle_rank(h))
    print(rs, rr)
    print(recognize(h))

