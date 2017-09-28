from array_utils import shuffle
import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def getDeck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = rank + ' of ' + suit
            deck += [card]
    return deck

def get_hand(deck):
    return random.sample(deck,5)



if __name__ == "__main__":
    deck = getDeck()

    print(deck)
    print(shuffle(deck))
    print(get_hand(deck))
