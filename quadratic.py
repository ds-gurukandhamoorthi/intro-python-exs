import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = b**2 - 4.0*a*c
if discriminant < 0:
    print('discriminant negative : no real solutions')
elif a == 0:
    print('not a second degree equation')
else:
    d=math.sqrt(discriminant)
    print('solutions are')
    print((-b+d)/(2*a))
    print((-b-d)/(2*a))


