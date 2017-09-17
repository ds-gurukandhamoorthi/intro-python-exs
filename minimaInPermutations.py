import sys
from arrayUtils import shuffle
def leftToRightMinima(array,stopAt=None):
    mini = array[0]
    nbMiniSoFar = 1
    for val in array[1:]:
        if  val < mini:
            mini = val
            nbMiniSoFar += 1
        if val == stopAt:
            return nbMiniSoFar
    return nbMiniSoFar

if __name__ == "__main__":
    n = int(sys.argv[1])
    nbTrials = int(sys.argv[2])
    count = 0
    for i in range(nbTrials):
        perm = shuffle(list(range(n)))
        count += leftToRightMinima(perm,0)
    print(count/nbTrials)

    # print(leftToRightMinima([4,6,3,5,1,2]))
    # print(leftToRightMinima([3,1,2]))
    # print(leftToRightMinima([3,2,1]))
