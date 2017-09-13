import cards
import sys

NB_CARDS_PER_PLAYER = 5
nbPlayers = int(sys.argv[1])

def printHand(deck,nb=1):
    for i in range(nb):
        print('\n'.join(deck[0:5]))
        deck = deck[5:]
        print('')
    return deck
        
        
        

if __name__ == "__main__":
    # print(cards.shuffle(cards.getDeck()))
    deck = cards.shuffle(cards.getDeck())
    printHand(deck,nbPlayers)
