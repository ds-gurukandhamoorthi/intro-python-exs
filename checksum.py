import sys

n = int(sys.argv[1])
n_ = n

checksum = 0
for i in range(9,0,-1):
    digit = int(n // 10**(i-1))
    checksum += (11-i)*digit
    n -= digit * 10**(i-1)

print(checksum%11,n_,sep='')



