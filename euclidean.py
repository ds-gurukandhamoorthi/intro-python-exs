import math

def euclideanDist(va, vb):
    n = max(len(va),len(vb))
    total = 0
    for i in range(n):
        total += (va[i]-vb[i])**2
    return math.sqrt(total)

if __name__ == "__main__":
    print(euclideanDist([0,0,0],[1,1,1]))
    print(euclideanDist([2,-1],[-2,2]))
    print(euclideanDist([1.23209,-370.67322 ],[1.18702,-375.09202]))
