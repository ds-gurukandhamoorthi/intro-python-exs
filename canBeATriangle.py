import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

res = not((  c >= a + b ) or (b >= a + c ) or ( a >= b + c ))
print(res)
