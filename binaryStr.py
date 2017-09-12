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
res = ''
for i in range(maxpower, -1, -1):
    divd = n//k**i
    if(divd == 10):
        res+='A'
    elif(divd == 11):
        res+='B'
    elif(divd == 12):
        res+='C'
    elif(divd == 13):
        res+='D'
    elif(divd == 14):
        res+='E'
    elif(divd == 15):
        res+='F'
    else:
        res += str(divd)
    n -= (k**i )*divd
print(res)
