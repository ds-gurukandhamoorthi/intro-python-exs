import os
import argparse
from Vector import Vector
from array_utils import aperture



class Sketch:
    def __init__(self, text, k, d):
        freq = [0] * d
        for kgram in aperture(text, k):
            h = hash(kgram)
            freq[h%d] += 1
        self._sketch = Vector(freq).direction()

    def similar_to(self, other):
        return self._sketch * other._sketch

    def __str__(self):
        return str(self._sketch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the Skecth of a text document')
    parser.add_argument('filename',  help='name of the text file')
    parser.add_argument('k', type=int, help='k as in kgrams')
    parser.add_argument('d', type=int, help='dimension : how fine-grained is your reality?')
    args = parser.parse_args()
    filename = args.filename
    k = args.k
    d = args.d
    with open(filename) as f:
        text = f.read()
        sk = Sketch(text, k, d)
        print(sk)
    f1 = open('../corpus/prejudice.txt')
    s1 = Sketch(f1.read(), k, d)
    f2 = open('../corpus/constitution.txt')
    s2 = Sketch(f2.read(), k, d)
    print(s1.similar_to(s2))


