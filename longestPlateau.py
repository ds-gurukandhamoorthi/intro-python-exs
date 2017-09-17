from rle import rleAndIndex
def getPlateaus(array):
    def inThisOrder(a,b,c):
        return a[1]<b[1]<c[1]
    rlei = rleAndIndex(array)
    res = []
    for i in range(1,len(rlei)-1):
        if inThisOrder(rlei[i-1],rlei[i],rlei[i+1]):
            res += [rlei[i]]
    return res

def longestPlateau(array):
    plateaus = getPlateaus(array)
    oneLongestPlateau = max(plateaus)
    return (oneLongestPlateau[2],oneLongestPlateau[0])


if __name__ == "__main__":
    print(getPlateaus('aabc'))
    print(getPlateaus('aabbc'))
    print(longestPlateau('aabbc'))
    print(longestPlateau([1,2,3,4,4,4,5,5,6]))
