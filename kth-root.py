import sys

eps = 10**-7

c = float(sys.argv[1])
k = int(sys.argv[2])
t = c
# while abs(t - c/t) > (eps*(k-1)*t):
while True:
    t0 = t
    t = ((k-1)*t + c/(t**(k-1)))/k
    if abs(t - t0) < eps:
        break
    print(t)
print(t)
