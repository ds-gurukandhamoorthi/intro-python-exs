import math
from functools import reduce
from operator import sub

def euclideanDist(va, vb):
    return math.sqrt(squared_distance(va,vb))

def squared_distance(va, vb):
    n = max(len(va),len(vb))
    total = 0
    for i in range(n):
        total += (va[i]-vb[i])**2
    return total

def chebyschevDist(va, vb):
    n = max(len(va),len(vb))
    return max([abs(va[i]-vb[i]) for i in range(n)])
            
def chebyschevDist2(va, vb):
    return max(abs(a-b) for a,b in zip(va,vb))

def chebyschevDist3(va, vb):
    diff = map(sub, va,vb) # A-B
    absltValuesOfDiff = map(abs,diff) # |A-B|
    return max(absltValuesOfDiff)

if __name__ == "__main__":
    print(euclideanDist([0,0,0],[1,1,1]))
    print(euclideanDist([2,-1],[-2,2]))
    print(euclideanDist([1.23209,-370.67322 ],[1.18702,-375.09202]))
    print(chebyschevDist([2,-1],[-2,2]))
    print(chebyschevDist([4,6],[5,2]))
    print(chebyschevDist2([4,6],[5,2]))
    print(chebyschevDist3([4,6],[5,2]))
