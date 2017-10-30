import sys
import random
import timeit

def triplets_having_sum_closest(lst, total=0):
    n = len(lst)
    res = None
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x, y, z = lst[i], lst[j], lst[k]
                if res is None:
                    res = (x, y, z)
                elif abs(x + y + z - total) < abs(sum(res) - total):
                    return (x, y, z)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename) as ints:
            lst_ints = ints.read().split('\n')[1:]
            lst_ints = [int(i.strip()) for i in lst_ints if i != '']
            print(triplets_having_sum_closest(lst_ints, 0))



if __name__ == "__main__":
    main()
