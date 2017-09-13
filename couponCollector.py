import random
import sys


n = int(sys.argv[1])
nbTrials = int(sys.argv[2])



def couponCollector(n):
    notYetCollected = [True]*n
    count = 0
    steps = 0
    while count < n:
        steps += 1
        samp = random.randrange(0,n)
        if notYetCollected[samp]:
            notYetCollected[samp] = False
            count += 1
    return steps

totalSteps = 0
for i in range(0,nbTrials):
    totalSteps += couponCollector(n)

print(totalSteps/nbTrials)






