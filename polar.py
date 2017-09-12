import sys, math

x = float(sys.argv[1])
y = float(sys.argv[2])

print("angle " + str(math.atan2(y,x)))
print("amplitude " + str(math.sqrt(x**2+y**2)))
