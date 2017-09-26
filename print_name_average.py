from ioutils import read_strings
from strutils import words

if __name__ == "__main__":
    array = read_strings()
    for line in array:
        words_array = words(line)
        name = ' '.join(words_array[0:-2])
        a = int(words_array[-2])
        b = int(words_array[-1])
        res = a/b
        print('%25s' % name, '%3d' % a, '%3d' % b, '%3.3f' % res)

        



