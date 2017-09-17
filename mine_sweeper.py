import sys
import random
import printBoolArray

def create_mine(m,n,p):
    a = [[False]*(n+2) for i in range(m+2)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if random.random() < p:
                a[i][j] = True
    return a
def count_mines(m,n, bombs):
    count = [[0]*(n+2) for i in range(m+2)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if bombs[i][j]:
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x == 0 and y == 0:
                            continue
                        count[i+x][j+y] += 1
    return count

if __name__ == "__main__":
    m = int(sys.argv[1]) 
    n = int(sys.argv[2])
    p = float(sys.argv[3])
    bombs = create_mine(m, n, p)
    count = count_mines(m, n, bombs)
    printBoolArray.printMatrix(bombs, "*", ".")
    print('')
    for i in range(1,m+1):
        for j in range(1,n+1):
            if bombs[i][j]:
                print('* ', end='')
            else:
                print(str(count[i][j])+' ',end='')
        print('')

