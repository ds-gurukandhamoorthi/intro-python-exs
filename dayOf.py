import sys

d = int(sys.argv[1])
m = int(sys.argv[2])
y = int(sys.argv[3])

y0  = y- (14 - m ) //12
# print(y0)
x = y0 + y0//4 - y0//100 + y0//400
# print(x)
m0 = m + 12 *((14-m)//12) -2
# print(m0)
d0 = (d + x + (31*m0)//12) % 7
print(d0)


