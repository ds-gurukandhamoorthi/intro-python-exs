import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

maxi = max(a,b,c)
mini = min(a,b,c)
leftOut = a + b + c - maxi -mini

print(mini, leftOut, maxi)
