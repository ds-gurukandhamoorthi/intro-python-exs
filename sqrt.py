import sys

eps = 10**-15

c = float(sys.argv[1])
t = c
while abs(t - c/t) > (eps*t):
    t = (t + c/t)/2
    print(t)
print(t)
