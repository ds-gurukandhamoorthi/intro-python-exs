import random


def binary_search(array, elem, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array)
    m = (start + end) // 2
    if start > end:
        return -1
    if array[m] == elem:
        return m
    if elem < array[m]:
        return binary_search(array, elem, start, m - 1)
    return binary_search(array, elem, m + 1, end)

def binary_search_iter(array, elem):
    start = 0
    end = len(array)
    while start <= end:
        m = (start + end) // 2
        if array[m] == elem:
            return m
        if elem < array[m]:
            end = m - 1
        else:
            start = m + 1
    return -1

def binary_search_min_index(array, elem, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array)
    m = (start + end) // 2
    if start > end:
        return -1
    if array[m] == elem:
        for j in reversed(range(m+1)):
            print(j, array[j], elem)
            if array[j] == elem:
                m_ = j
        return m_
    if elem < array[m]:
        return binary_search(array, elem, start, m - 1)
    return binary_search(array, elem, m + 1, end)


def main():
    a = sorted([random.randrange(10) for i in range(10)])
    print(a)
    i = random.randrange(len(a))
    print(i, a[i])
    print(binary_search(a, a[i]))
    print(binary_search_iter(a, a[i]))
    print(binary_search_min_index(a, a[i]))


if __name__ == "__main__":
    main()
