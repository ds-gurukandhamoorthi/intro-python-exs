import sys
sys.path.append('../')
import stdio

n = int(sys.argv[1])
total = 0
for i in range(n):
    total += int(input())
print(total)
