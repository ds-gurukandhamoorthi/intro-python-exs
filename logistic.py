import sys


x = float(sys.argv[1])

r = float(sys.argv[2])


gen = 0
while 0 < x < 1:
    gen += 1
    x_ = x
    x = r*x*(1-x)
    if abs(x - x_) < 0.0001:
        break

print(gen , x_,x)




