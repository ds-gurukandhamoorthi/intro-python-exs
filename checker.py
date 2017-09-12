import sys
n = int(sys.argv[1])

for i in range(0,n):
    for j in range(0,n*2):
        if((i+j)%2==0):
            print('*',end='')
        else:
            print(' ',end='')
    print('')
