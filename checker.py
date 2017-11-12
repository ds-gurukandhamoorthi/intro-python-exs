import sys
n = int(sys.argv[1])

for i in range(n):
    for j in range(n*2):
        if((i+j)%2==0):
            print('*',end='')
        else:
            print(' ',end='')
    print('')
