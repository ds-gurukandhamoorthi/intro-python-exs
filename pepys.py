import random
import sys

nbTrials = int(sys.argv[1])


def die():
    return random.randrange(1,7)

def obtain(attainCount, nbDiceRolls):
    count = 0
    for i in range(0,nbDiceRolls):
        if die()==1:
            count += 1
            if count >=attainCount:
                return True
    return False
def obtain1twiceRoll12():
    return obtain(2, 12)
def obtain1Roll6():
    return obtain(1,6)


obt1in6=0
obt1twicein12=0
for i in range(0,nbTrials):
    if obtain1Roll6():
        obt1in6 += 1
    if obtain1twiceRoll12():
        obt1twicein12 += 1


print(obt1in6/nbTrials, obt1twicein12/nbTrials)
     
        
