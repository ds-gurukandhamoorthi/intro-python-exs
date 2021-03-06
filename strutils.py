import re
from collections import Counter
from math import log
from array_utils import shannon_entropy_list, aperture
def words(str):
    return [ word for word in  re.split('\s+',str) if word !='']


def is_palindrome(s):
    n = len(s)
    return all(s[i] == s[n-1-i] for i in range(n//2))

def is_sorted(array):
    return all(array[i] < array[i+1] for i in range(len(array)-1))

def shift(string, num):
    return string[num:] + string[:num]

#not as performant as the string concatenation method
def is_circular_shift_of_(string1, string2):
    n = len(string1)
    for i in range(n):
        if shift(string1,i) == string2:
            return True
    return False

def is_circular_shift_of(string1, string2):
    return string1 in string2*2

def domain_type(url):
    domain= url.split('/')[2]
    return domain.split('.')[-1]

def inverse_domain(domain):
    return split_and_reverse(domain, '.')

def split_and_reverse(string, sep):
    return sep.join(reversed(string.split(sep)))

#it reverses string by swapping recursively
def mystery(s):
    n = len(s)
    if n <= 1:
        return s
    return mystery(s[n//2:]) + mystery(s[:n//2])

def substrings_win(s, window):
    assert window > 0
    # return (s[i:i+window] for i in  range(len(s)-window+1))
    yield from (''.join(chars) for chars in aperture(s, window))

def substrings(s):
    n = len(s)
    res = []
    for i in range(n+1):
        for j in range(i):
            res += [''.join(s[j:i])]
    return res


def possible_genes(s, min_length):
    assert min_length > 0
    yield from (s[i:] for i in  range(len(s)-min_length+1))

def substring_prefix_suffix(prefix, suffix, string):
    res = []
    for s in substrings(string):
        if prefix not in s and suffix not in s:
            res += [prefix+s+suffix]
    return res

def shannon_entropy(string):
    return shannon_entropy_list(list(string))

def metric_entropy(string):
    return shannon_entropy(string)/len(string)

def unique_substrings(string, length):
    return set(list(substrings_win(string, length)))





def test_words():
    assert(words('The quick brown fox') == ['The', 'quick', 'brown', 'fox'])
    assert(words(' The quick brown fox') == ['The', 'quick', 'brown', 'fox'])
