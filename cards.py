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

deck = getDeck()

def shuffle(deck):
    n = len(deck)
    for i in range(n):
        r = random.randrange(i,n)
        deck[i], deck[r] = deck[r],deck[i]
    return deck

if __name__ == "__main__":
    print(random.sample(deck,5))

    print(deck)
    print(shuffle(deck))
    print(random.sample(range(5),3))
