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

def dimen(matrix):
    return (len(matrix), len(matrix[0]))

def matrMultBool(a, b):
    "Multiplies two boolean matrix * becomes 'and' + becomes 'or'"
    l = len(a)
    c = len(b[0])
    common = len(a[0]) #len(a[0]) must be len(b)
    if(len(a[0])!=len(b)):
        return []
    res = [[False]*c for i in range(l)]
    print("dim res" + str(dimen(res)))
    print("dim a" + str(dimen(a)))
    print("dim b" + str(dimen(b)))
    for i in range(l):
        for j in range(c):
            resval = False
            for k in range(common):
                resval = resval or (a[i][k] or b[k][j])
            res[i][j]=resval
    return res


print(matrMultBool(a,b))
print(matrMultBool(c,c))
print("c")
printBoolArray.printMatrix(c)
print("d")
printBoolArray.printMatrix(d)
print(matrMultBool(c,d))
# print(matrMultBool(d,c))
print(matrMultBool(e,f))
