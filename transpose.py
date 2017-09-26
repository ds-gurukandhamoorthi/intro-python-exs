from matrixutils import transpose

a = [[99,85,98],
        [34,90,23],
        [23,45,94],
        [13,84,74],
        [34,65,97]]


def transposeInplace(squareArray):
    n = len(squareArray)
    for i in range(n):
        for j in range(i):
            if i != j:
                squareArray[i][j],squareArray[j][i]=squareArray[j][i],squareArray[i][j]
    return squareArray

    


print(a)
print(transpose(a))
print(transpose(transpose(a)))

sqr = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(transposeInplace(sqr))
print(transposeInplace(sqr))
