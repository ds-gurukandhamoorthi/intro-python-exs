import sys, math
import random

n = int(sys.argv[1])
summ = 0
maxi  = 0
mini = 0
for i in range(0,n+1):
    r = random.random();
    print(r)
    if i == 0:
        maxi = r
        mini = r
        summ = r
    else:
        maxi = max(r,maxi)
        mini = min(r,mini)
        summ += r

print(mini,maxi)
print(summ/n)
