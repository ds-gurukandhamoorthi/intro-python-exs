import sys, math

x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])


G = 9.80665
res = x0 + v0 * t + 0.5*G*t**2
print(res)
