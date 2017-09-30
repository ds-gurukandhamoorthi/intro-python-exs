from cards import get_hand
from rle import rle
from pprint import pprint
import argparse
from collections import Counter

# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
RANKS = list(range(0,13))
SUITS = ['C','D','H','S']

STRAIGHT_FLUSH='straight flush'
FLUSH = 'flush'
FULL_HOUSE="full house"
FOUR_OF_A_KIND="four of a kind"
THREE_OF_A_KIND="three of a kind"
TWO_PAIR="two pair"
ONE_PAIR="one pair"
STRAIGHT='straight'
HIGH_CARD='high card'


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

def get_pattern_suits(hand):
    return get_counts(rle_suit(hand))

def is_of_seq_rank(hand):
    rnks = sorted(get_ranks(hand))
    return rnks[-1] - rnks[0] == len(hand) - 1


def recognize(hand):
    ranks_ptrn = get_pattern_ranks(hand)
    suits_ptrn = get_pattern_suits(hand)
    sequential = is_of_seq_rank(hand)
    if sequential:
        if suits_ptrn == [5]:
            return STRAIGHT_FLUSH
        else:
            return STRAIGHT
    if suits_ptrn == [5]:
            return FLUSH
    if ranks_ptrn == [3, 2]:
        return FULL_HOUSE 
    if ranks_ptrn == [4, 1]:
        return FOUR_OF_A_KIND
    if ranks_ptrn == [3, 1, 1]:
        return THREE_OF_A_KIND
    if ranks_ptrn == [2, 2, 1]:
        return TWO_PAIR
    if ranks_ptrn == [2, 1, 1, 1]:
        return ONE_PAIR
    return HIGH_CARD

def simulate(nb_trials):
    DECK = get_deck_tuple()
    res = Counter((recognize(get_hand(DECK)) for i in range(nb_trials)))
    for k, v in res.items():
        res[k] = v/nb_trials
    return res





if __name__ == "__main__":
    h=get_hand(get_deck_tuple())
    # print(h)
    # print(get_suits(h))
    # print(rle_suit(h))
    # print(get_ranks(h))
    # rs = (rle_suit(h))
    # rr = (rle_rank(h))
    # print(rs, rr)
    # print(recognize(h))
    # print(get_pattern_ranks(ex_flush))
    # print(get_pattern_suits(ex_flush))
    # print(recognize(ex_flush))
    ex_flush= [('D',11), ('D',9), ('D',8),('D',4),('D',3)]
    assert recognize(ex_flush)==FLUSH
    ex_sequential= [('D',11), ('D',10), ('S',9),('S',7),('D',8)]
    assert is_of_seq_rank(ex_sequential) == True
    ex_straight_flush = [('D',11), ('D',10), ('D',9),('D',8),('D',7)]
    assert recognize(ex_straight_flush) == STRAIGHT_FLUSH
    ex_two_pair = [('H',11),('S',11),('C',3), ('S',3),('H',2)]
    assert recognize(ex_two_pair)== TWO_PAIR
    ex_one_pair = [('S',10),('H',10),('S',8), ('H',7),('C',4)]
    assert recognize(ex_one_pair)== ONE_PAIR
    ex_three_of_a_kind = [('C',12), ('S',12), ('H',12), ('H',9), ('S',2)]
    assert recognize(ex_three_of_a_kind) == THREE_OF_A_KIND
    ex_four_of_a_kind = [('S',5),('H',5),('C',5),('D',5),('D',2)]
    assert recognize(ex_four_of_a_kind) == FOUR_OF_A_KIND
    ex_full_house = [('S',6), ('H',6), ('D',6), ('C',13),('H', 13)]
    assert recognize(ex_full_house) == FULL_HOUSE
    ex_straight = [('D',10),('S',9),('H',8), ('D',7), ('C', 6)]
    assert recognize(ex_straight) == STRAIGHT
    ex_high_card = [('D',13), ('H', 12), ('S', 7), ('S', 4), ('H', 3)]
    assert recognize(ex_high_card) == HIGH_CARD

    parser = argparse.ArgumentParser(description='Simulate poker game')
    parser.add_argument('nb_trials', type=int, help='number of hands to analyze')
    args = parser.parse_args()
    nb_trials = args.nb_trials

    res = simulate(nb_trials)
    pprint(res)



