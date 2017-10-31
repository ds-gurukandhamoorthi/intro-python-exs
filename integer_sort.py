import random
from collections import Counter


def sort_integers(array, maximum=99):
    count = Counter(array)
    res = []
    for i in range(maximum + 1):
        res += [i] * count[i]
    return res


def main():
    a = [random.randrange(100) for i in range(100)]
    print(sort_integers(a))
    print(sort_integers(a)== sorted(a))


if __name__ == "__main__":
    main()
