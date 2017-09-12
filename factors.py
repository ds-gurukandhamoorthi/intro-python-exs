import sys

number = int(sys.argv[1])

i=2
n=number
while i*i <= number:
    while n % i == 0:
        while n % i == 0:
            n//=i
        print(i, end=' ')
    i+=1

if n > 1:
    print(n)


