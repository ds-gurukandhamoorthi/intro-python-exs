import sys
n = int(sys.argv[1])
sum = 0

for i in range(n+1):
    sum += i
print(sum)

print((n*(n+1))//2)
