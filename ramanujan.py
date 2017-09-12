import sys

n = int(sys.argv[1])

def cube(n):
    "calculates the cube of a number"
    return n * n * n

for i in range(1, n+1):
    if cube(i)>n:
        break
    for j in range(i, n+1):
        if cube(i)+cube(j)>n:
            break
        for k in range(1+i, n+1):
            if cube(k)>cube(i)+cube(j):
                break
            for l in range(k,n+1):
                if (cube(k)+cube(l) > cube(i)+cube(j)):
                    break
                if (cube(k)+cube(l) == cube(i)+cube(j)):
                    print(i, j, k, l, cube(k)+cube(l), cube(i)+cube(j))
