import sys
def permutation(lst):
    if len(lst) == 1:
        return [lst]
    res = []
    for i, val in enumerate(lst):
        perm_others = permutation(lst[:i]+lst[i+1:])
        res += [[val] + perm for perm in perm_others]
    return res

def permutation_size(lst, k):
    "Returns permutations of size k"
    if k == 0 or len(lst) < k:
        return [[]]
    # if k == 1:
    #     return [[x] for x in lst]
    res = []
    for i, val in enumerate(lst):
        perm_lesser_size = permutation_size(lst[:i]+lst[i+1:], k-1)
        res += [[val]+ perm for perm in perm_lesser_size]
    return res


def chars(n):
    return [chr(i+ord('a')) for i in  range(n)]

def str_perm(n):
    p = permutation(chars(n))
    return [''.join(l) for l in p]

def str_perm_size(n,k):
    p = permutation_size(chars(n),k)
    return [''.join(l) for l in p]

def combinations(lst):
    res =[]
    for i in range(len(lst)+1):
        res += combinations_of_length(lst,i)
    return res
        

def combinations_of_length(lst, k):
    if k <= 0:
        return [[]]
    res = []
    for i, val in enumerate(lst):
        comb_lesser_length = combinations_of_length(lst[i+1:],k-1)
        res += [[val] + comb for comb in comb_lesser_length]
    return res






if __name__ == "__main__":
    # n = 3
    # p = permutation([0,2])
    # print("p", p)
    # p = permutation([0,2,3])
    # print("p", p)
    # p = permutation(['a','b','c'])
    # print("p", [''.join(l) for l in p])
    # print(chars(26))
    print(*str_perm(4),sep='\n')
    # p = permutation_size(['a','b','c','d'],2)
    # print(p)
    print(*str_perm_size(4,2),sep='\n')
    print(permutation_size([1,3,2,4],2))
    print(combinations_of_length([1,3,2,4],2))
    print(combinations([1,3,2,4]))
        

