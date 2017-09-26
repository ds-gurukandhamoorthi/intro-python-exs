import sys
import re
from sys import stdin
from strutils import words

def count_words(line):
    return len(words(line))

if __name__ == "__main__":
    count = 0
    for line in stdin:
        line = line.strip()
        count += count_words(line)

    print(count)


