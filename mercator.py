import sys, math

lambda0 = float(sys.argv[1])
#longitude
lambda_ = float(sys.argv[2])
#latitude
phi = float(sys.argv[2])

x = lambda_ - lambda0
frac = (1+math.sin(phi))/ (1-math.sin(phi))
y = 0.5*math.log(frac)
print(x,y)

