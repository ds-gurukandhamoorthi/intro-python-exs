import argparse
import sys
from array_utils import shuffle, bad_shuffle
from riffle_shuffle import riffle_shuffle
import math

parser = argparse.ArgumentParser(description='Shuffle check empirical study')
parser.add_argument('n', type=int, help='number of elements to shuffle')
parser.add_argument('nbTrials', type=int, help='number of experiements')
args = parser.parse_args()
n = args.n
nbTrials = args.nbTrials

def trials(n, nbTrials,shufflingFunc):
    stat = [[0]*n for i in range(n)]
    for j in range(nbTrials):
        initial = [i for i in range(n)]
        shuffled = shufflingFunc(initial)
        for i in range(len(shuffled)):
            stat[shuffled[i]][i]+=1
    return stat

def distMatrixes(ma, mb):
    dis = 0
    for rowa, rowb in zip(ma,mb):
        for val1, val2 in zip(rowa,rowb):
            dis += (val1-val2)**2
    return math.sqrt(dis)

def applyShuffle(funcShuffle, n):
    def shuf(array):
        res=funcShuffle(array)
        for i in range(n-1):
            res = funcShuffle(res)
        return res
    return shuf

            

if __name__ == "__main__":
    # res=trials(n,nbTrials,bad_shuffle)
    # print(res)
    expected = [[nbTrials//n]*n for i in range(n)]
    # print(expected)
    resShuffle=trials(n,nbTrials,shuffle)
    resBadShuf =trials(n,nbTrials,bad_shuffle)
    resRiffle=trials(n,nbTrials,riffle_shuffle)
    resRiffleTwo=trials(n,nbTrials,applyShuffle(riffle_shuffle,2))
    resRiffle_3=trials(n,nbTrials,applyShuffle(riffle_shuffle,3))
    resRiffle_4=trials(n,nbTrials,applyShuffle(riffle_shuffle,4))
    resRiffle_5=trials(n,nbTrials,applyShuffle(riffle_shuffle,5))
    resRiffle_6=trials(n,nbTrials,applyShuffle(riffle_shuffle,6))
    resRiffle_7=trials(n,nbTrials,applyShuffle(riffle_shuffle,7))
    resRiffle_8=trials(n,nbTrials,applyShuffle(riffle_shuffle,8))
    resRiffle_9=trials(n,nbTrials,applyShuffle(riffle_shuffle,9))
    resRiffle_10=trials(n,nbTrials,applyShuffle(riffle_shuffle,10))
    resRiffle_11=trials(n,nbTrials,applyShuffle(riffle_shuffle,11))
    print(distMatrixes(expected,resShuffle))
    print(distMatrixes(expected,resBadShuf))
    print(distMatrixes(expected,resRiffle))
    print(distMatrixes(expected,resRiffleTwo))
    print(distMatrixes(expected,resRiffle_3))
    print(distMatrixes(expected,resRiffle_4))
    print(distMatrixes(expected,resRiffle_5))
    print(distMatrixes(expected,resRiffle_6))
    print(distMatrixes(expected,resRiffle_7))
    print(distMatrixes(expected,resRiffle_8))
    print(distMatrixes(expected,resRiffle_9))
    print(distMatrixes(expected,resRiffle_10))
    print(distMatrixes(expected,resRiffle_11))

            






