import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

a,b = abs(a), abs(b)
a,b = max(a,b), min(a,b)

gcd = 1
while True:
    if a%b ==0:
        gcd = b
        break
    else:
        a,b = b, a%b

print(gcd)

def gcd(a,b):
    "Calculates the greatest common divisor of a number"
    a,b = abs(a), abs(b)
    a,b = max(a,b), min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

print(gcd(a,b))

        
