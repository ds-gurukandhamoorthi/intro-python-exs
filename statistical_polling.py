import sys
from ioutils import read_strings
import random

nbSample = int(sys.argv[1])

array = read_strings()
samp = random.sample(array, nbSample)
for el in samp:
    print(el)
