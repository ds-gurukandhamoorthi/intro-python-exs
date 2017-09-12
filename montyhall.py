import sys
import random

n = int(sys.argv[1])


def oneGame():
    prize = random.randrange(0,3)
    choice = random.randrange(0,3)
    opened = prize
    while opened == choice or opened == prize:
        opened = random.randrange(0,3)
    other = 0 + 1 + 2 - opened - choice
    if other == prize:
        return True

count = 0
for i in range(0,n):
    if oneGame():
        count += 1

print(count/n)


