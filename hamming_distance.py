import argparse
from permutations import combinations_of_length

def flip(bit):
    return {'0':'1','1':'0'}[bit]

def flip_bits(string, lst):
    new_string = ""
    for i, bit in enumerate(string):
        if i in lst:
            new_string += flip(string[i])
        else:
            new_string += string[i]
    return new_string

def within_hamming_dist(string, dist):
    n = len(string)
    change_bits = combinations_of_length(list(range(n)), dist)
    res = []
    for change in change_bits:
        res += [flip_bits(string, change)]
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Strings having a hamming distance lesser thant he string given')
    parser.add_argument('string', help='bit string')
    parser.add_argument('dist', type=int, help='hamming distance from the given string')
    args = parser.parse_args()
    string = args.string
    dist = args.dist
    res =within_hamming_dist(string, dist)
    print(*res,sep='\n')

