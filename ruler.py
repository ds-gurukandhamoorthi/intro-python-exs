import sys
import matplotlib.pyplot as plt

def ruler_iter(n):
    ruler = [1]
    for i in range(2,n+1):
        ruler = ruler + [i] + ruler 
    return ruler

def ruler_rec(n):
    if n <= 1:
        return [1]
    prev = ruler_rec(n-1)
    return prev + [n] + prev

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(*ruler_rec(n))
    print(*ruler_iter(n))
    res = ruler_iter(n)
    plt.bar(range(len(res)), res)
    plt.axis('off')
    plt.show()
