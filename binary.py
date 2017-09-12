import sys
import math


n = int(sys.argv[1])
k = int(sys.argv[2])
if n == 0: 
    maxpower = 0
else:
    maxpower = int(math.log(n,k));
# print(maxpower)
binstr = '';

for i in range(maxpower, -1, -1):
    divd = n//k**i
    if(divd == 10):
        print('A', end='')
    elif(divd == 11):
        print('B', end='')
    elif(divd == 12):
        print('C', end='')
    elif(divd == 13):
        print('D', end='')
    elif(divd == 14):
        print('E', end='')
    elif(divd == 15):
        print('F', end='')
    else:
        print(divd, end='')
    n -= (k**i )*divd
print('')
