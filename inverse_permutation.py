import sys

def contains_distinct_elems(array):
    "Tells if an array of length n contains n distinct values"
    seen = [False] * len(array)
    for val in array:
        if seen[val]:
            return False
        seen[val] = True
    return True

def is_valid_perm(array):
    "Tells if an array is a valid permutation starting with 0"
    return sorted(array)==list(range(len(array)))

def inverse_perm(array):
    "Invereses a permutaion"
    inv = [0] * len(array)
    for i, val in enumerate(array):
        inv[val] = i
    return inv




if __name__ == "__main__":
    perm = []
    for i in range(1,len(sys.argv)):
        perm += [int(sys.argv[i])]

    if is_valid_perm(perm):
        print(perm)
        print(inverse_perm(perm))
    else:
        print("not a valid permutation")


    # print(is_valid_perm([0, 2, 1]))
    # print(is_valid_perm([0, 0, 1]))
    # print(inverse_perm([1,4,3,2,0]))


