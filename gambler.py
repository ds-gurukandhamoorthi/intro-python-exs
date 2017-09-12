import sys
import random

initial = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
prob = float(sys.argv[4])
maxBets = int(sys.argv[5])

amount = initial

wins = 0
bets = 0
i = 0
while i <= trials:
    amount = initial
    thisBets = 0
    while 0 < amount < goal and thisBets <= maxBets:
        if random.random() <= prob:
            amount += 1
        else:
            amount -= 1
        bets += 1
        thisBets += 1
        print("*" * amount)
    if amount >=goal:
        wins += 1
    i+=1
    print('')

print(wins/trials)
print(bets//trials)
    
