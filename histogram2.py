def histogram(array, m):
    res = [0] * m
    for val in array:
        res[val] += 1
    return res
if __name__ == "__main__":
    a=[1, 0, 1, 1, 0, 1,0, 0,0,2]
    his = histogram(a, 3)
    print(his)
    print(len(a), sum(his))
