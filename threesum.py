import sys
import random
import timeit
from itertools import combinations


def triplets_having_sum_ERRONEOUS(lst, total=0):
    for i, x in enumerate(lst):
        for j, y in enumerate(lst[i + 1:]):
            for k, z in enumerate(lst[j + 1:]):
                if x + y + z == total:
                    yield (x, y, z)


def triplets_having_sum(lst, total=0):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x, y, z = lst[i], lst[j], lst[k]
                if x + y + z == total:
                    yield (x, y, z)


def nuplets_having_sum(n, lst, total=0):
    # yield from (c for c in combinations(lst, n) if sum(c) == total)
    expected_total = lambda c: sum(c) == total
    yield from filter(expected_total, combinations(lst, n))


def rand_ints(n):
    MAX = 1000000
    return [random.randrange(-MAX, MAX + 1) for i in range(n)]


def trial(nb):
    lst = rand_ints(nb)
    # print(list(triplets_having_sum(lst, 0)))
    print(list(nuplets_having_sum(3, lst, 0)))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename) as ints:
            lst_ints = ints.read().split('\n')[1:]
            lst_ints = [int(i.strip()) for i in lst_ints if i != '']
            print(list(triplets_having_sum(lst_ints, 0)))
            # print(list(nuplets_having_sum(3, lst_ints, 0)))
    else:
        for i in range(10):
            nb = 256 * 2**(i)
            time_taken = timeit.timeit(
                'trial(' + str(nb) + ')', setup='from threesum import trial', number=1)
            print(nb, time_taken)


if __name__ == "__main__":
    main()
