import random
from array_utils import shuffle
from itertools import product, starmap

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def getDeck():
    name = lambda rank, suit: rank + ' of ' + suit
    return list(starmap(name, product(RANKS, SUITS)))


def get_hand(deck):
    return random.sample(deck, 5)


def main():
    deck = getDeck()

    print(deck)
    print(shuffle(deck))
    print(get_hand(deck))


if __name__ == "__main__":
    main()
