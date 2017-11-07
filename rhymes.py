from strutils import words

def reverse_strings(array):
    yield from (''.join(reversed(string)) for string in array)

def main():
    filename = '/usr/share/dict/words'
    words_list = []
    with open(filename) as inp:
        for line in inp:
            words_list += words(line)
    reversed_words = reverse_strings(words_list)
    res = reverse_strings(sorted(reversed_words))
    for word in res:
        print(word)



if __name__ == "__main__":
    main()
