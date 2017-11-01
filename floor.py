from itertools import takewhile, combinations, starmap
from collections import Counter
from array_utils import aperture


def floor(sorted_array, elem):
    def lt(x):
        return x < elem
    return len(list(takewhile(lt, sorted_array))) - 1


def ceiling(sorted_array, elem):
    def le(x):
        return x <= elem
    return len(list(takewhile(le, sorted_array)))


def bitonic_search_max(array, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array)
    m = (start + end) // 2
    if start > end:
        return -1
    if array[m - 1] <= array[m] and array[m] >= array[m + 1]:
        return m
    if array[m - 1] > array[m]:
        return bitonic_search_max(array, start, m)
    return bitonic_search_max(array, m, end)


def closest_pair_(array):
    def dist(x, y):
        return abs(x - y)
    res = None
    for x, y in combinations(array, 2):
        if res is None:
            res = (x, y)
        elif dist(*res) > dist(x, y):
            res = (x, y)
    return res


def sum_nuplets(array, n):
    def sum_and_tuple(tupl):
        return (sum(tupl), tupl)
    return map(sum_and_tuple, combinations(array, n))


def dist_pairs(array):
    def dist(x, y):
        return (abs(x - y), (x, y))
    return starmap(dist, combinations(array, 2))


def closest_pair(array):
    return min(dist_pairs(array))[1]


def furthest_pair(array):
    return max(dist_pairs(array))[1]


def two_sum(array):
    for tot, pair in sum_nuplets(array, 2):
        if tot == 0:
            return pair
    return None


def three_sum(array):
    for tot, triplet in sum_nuplets(array, 3):
        if tot == 0:
            return triplet
    return None


def majority(array):
    count = Counter(array)
    return count.most_common(1)[0][1] > sum(count.values()) / 2

def common_element(array1, array2, array3):
    common = Counter(array1) & Counter(array2) & Counter(array3)
    return len(common) >= 1

def largest_empty_interval(array):
    def dist(x, y):
        return (abs(x - y), (x, y))
    dists = starmap(dist, aperture(sorted(array),2))
    return min(dists)[1]

def prefix_free(array):
    def is_either_prefix(str1, str2):
        return str1.startswith(str2) or str2.startswith(str1)
    one_prefix_of_another = starmap(is_either_prefix, combinations(array ,2))
    return not any(one_prefix_of_another)


    


def main():
    a = [1, 2, 3, 5, 6, 7]
    print(floor(a, 4))
    print(ceiling(a, 4))
    b = [1, 5, 6, 10, 3]
    print(bitonic_search_max(b))
    print(min(dist_pairs(b)), max(dist_pairs(b)))
    print(closest_pair(b))
    print(furthest_pair(b))
    print(list(sum_nuplets(b, 2)))
    b = [-1, 5, 6, 10, 3, -2]
    print(two_sum(b))
    print(three_sum(b))
    b = [1, 2, 1, 3, 1,-4]
    print(majority(b))
    print(common_element(a, b, a))
    print(sorted(b))
    print(list(largest_empty_interval(b)))
    print(prefix_free(['01','10','0010','1010']))
    print(prefix_free(['01','10','0010','1110']))


if __name__ == "__main__":
    main()
