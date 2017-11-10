import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
e = int(sys.argv[5])

if a > b:
    a, b = b, a
    print(a, b, c, d, e)
if c > d:
    c, d = d, c
    print(a, b, c, d, e)
if b > d:
    b, d = d, b
    print(a, b, c, d, e)
if a > c:
    a, c = c, a
    print(a, b, c, d, e)
if b > c:
    b, c = c, b
    print(a, b, c, d, e)

if e >= d:
    print(c)
elif e >= c:
    print(c)
elif e <= b:
    print(b)
