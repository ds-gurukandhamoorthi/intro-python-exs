import sys
import re
from sys import stdin

def words(str):
    def remove_empty_strings(listelems):
        return list(filter(lambda x: x != '', listelems))
    res = re.split('\s+',str)
    return remove_empty_strings(res)

def count_words(line):
    return len(words(line))

if __name__ == "__main__":
    count = 0
    for line in stdin:
        line = line.strip()
        count += count_words(line)

    print(count)


