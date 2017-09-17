from arrayUtils import shuffle

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def getDeck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = rank + ' of ' + suit
            deck += [card]
    return deck



if __name__ == "__main__":
    deck = getDeck()

    print(deck)
    print(shuffle(deck))
