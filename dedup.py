import sys
from frequency_count import frequency_count



def main():
    filename = sys.argv[1]
    word_count = frequency_count(filename)
    for word in sorted(word_count.keys()):
        print(word)

if __name__ == "__main__":
    main()

