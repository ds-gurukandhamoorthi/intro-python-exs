import sys
from array_utils import shuffle

n = int(sys.argv[1])
nbTrial = int(sys.argv[2])

def musicTrial(n):
    "calculate prob of sequential song in a music player with shuffle"
    a = [i for i in range(n)]
    shuffled = shuffle(a)
    sequential = 0
    for i in range(len(a)-1):
        if a[i+1]-a[i] == 1:
            sequential += 1
    return sequential
        
countSeq = 0
for i in range(nbTrial):
    countSeq += musicTrial(n)

print(countSeq,n, nbTrial, countSeq/(n*nbTrial))


