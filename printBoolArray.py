
def printMatrix(matr):
    for i in range(len(matr)):
        print(i+1,end='')
    print('')
    i=0
    for row in matr:
        for v in row:
            toprint = '*' if v else ' '
            print(toprint, end='')
        print(i+1)
        i+=1

a = [[True, True, True, True],
        [False, False, True, True],
        [True, False, True, False],
        [False, False, False, False]]
if __name__ == "__main__":
    printMatrix(a)
