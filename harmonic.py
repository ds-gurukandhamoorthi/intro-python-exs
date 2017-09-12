import sys

n = int(sys.argv[1])

harmonicSum = 1

for i in range(2, n+1):
    harmonicSum += 1/i

print(harmonicSum)
    
