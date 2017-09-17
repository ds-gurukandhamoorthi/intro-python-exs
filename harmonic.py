import sys

n = int(sys.argv[1])

# harmonicSum = 1

# for i in range(2, n+1):
#     harmonicSum += 1/i

# print(harmonicSum)

def harmonicSum(n):
    harmsum = [0.0]*(n+1)
    for i in range(1,n+1):
        harmsum[i]=harmsum[i-1] + 1/i
    return harmsum[n]

print(harmonicSum(n))


