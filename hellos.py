import sys
n = int(sys.argv[1])

for i in range(1,n+1):
    if(i%100 == 11):
        print(str(i) +'th hello')
    elif (i%100 == 12):
        print(str(i) +'th hello')
    elif (i%100 == 13):
        print(str(i) +'th hello')
    elif(i%10 == 1):
        print(str(i) +'st hello')
    elif (i%10 == 2):
        print(str(i) +'nd hello')
    elif (i%10 == 3):
        print(str(i) +'rd hello')
    else:
        print(str(i) +'th hello')

