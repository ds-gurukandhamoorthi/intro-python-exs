import sys
from sys import stdin
from ioutils import read_ints


array = read_ints()

for i,val in enumerate(array):
    print('%3d' % val, end='\t')
    if  i %10 == 9:
        print('')

