import sys

n = int(sys.argv[1])

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j%i==0 or i%j==0):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print(i)

i=1
while i <=n:
    j=1
    while j <=n:
        if(j%i==0 or i%j==0):
            print('*',end='')
        else:
            print(' ',end='')
        j+=1
    print(i)
    i+=1
