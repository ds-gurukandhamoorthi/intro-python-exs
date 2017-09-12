import random
import math

r = random.random()
theta = random.random() * math.pi * 2
print (r, theta)
print (r, math.degrees(theta))
x,y= (r*(math.cos(theta)), r*(math.sin(theta)))
print(x,y)


a, b, c = 2*x*math.sqrt(1-x**2-y**2), 2*y*math.sqrt(1-x**2-y**2), 1-2*(x**2+y**2)

print(a,b,c)

