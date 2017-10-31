import sys
from collections import Counter
from strutils import words
import matplotlib.pyplot as plt


def frequency_count(filename):
    word_count = Counter()
    with open(filename) as inp:
        for line in inp:
            for word in words(line):
                word_count[word] += 1
    return word_count


def main():
    filename = sys.argv[1]
    word_count = frequency_count(filename)
    nb_words = sum(word_count.values())
    freqs = [count / nb_words for _, count in word_count.most_common()]
    zipf = [1 / i for i in range(1, len(freqs) + 1)]
    plt.plot(freqs, zipf)
    plt.show()
    for i, (word, count) in enumerate(word_count.most_common()):
        freq = count / nb_words
        print(freq, 1 / (i + 1), word, sep='\t')


if __name__ == "__main__":
    main()
