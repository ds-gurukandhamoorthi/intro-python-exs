import re
def words(str):
    def remove_empty_strings(listelems):
        # return list(filter(lambda x: x != '', listelems))
        return [s for s in listelems if s != '']
    res = re.split('\s+',str)
    return remove_empty_strings(res)


def is_palindrome(s):
    n = len(s)
    return all((s[i] == s[n-1-i] for i in range(n//2)))

def is_sorted(array):
    return all((array[i] < array[i+1] for i in range(len(array)-1)))
