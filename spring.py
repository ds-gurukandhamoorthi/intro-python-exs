import sys, math

d = int(sys.argv[1])
m = int(sys.argv[2])

res = (m == 3 and d >= 20 and  d <= 31 ) or (m == 4 and ( 1 <= d <= 30)) or (m == 5 and ( 1 <= d <= 31)) or(m == 6 and ( 1 <= d <= 20))
print(res)

