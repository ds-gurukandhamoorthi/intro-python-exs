from matrixutils import matrMultBool, matrMult, dimen
import printBoolArray

a=[[True,False],
        [False,True]]

b=[[True,False],
        [False,True]]

c = [[False,False],
    [False,False],
    [False,False]
    ]
d = [[False,False,False,True],
    [True,False, False,False]]

e = [[False,False],
        [False,False]]
f = [[False,False],
        [True,False]]




print(matrMultBool(a,b))
print(matrMultBool(c,c))
print("c")
printBoolArray.printMatrix(c)
print("d")
printBoolArray.printMatrix(d)
print(matrMultBool(c,d))
# print(matrMultBool(d,c))
print(matrMultBool(e,f))

a=[[1,2],
        [3,4],
        [5,6]]
b=[[5,6],
        [7,8]]
print(matrMult(a,b))

