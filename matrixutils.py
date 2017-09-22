
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
    # print("dim res" + str(dimen(res)))
    # print("dim a" + str(dimen(a)))
    # print("dim b" + str(dimen(b)))
    for i in range(l):
        for j in range(c):
            resval = False
            for k in range(common):
                resval = resval or (a[i][k] or b[k][j])
            res[i][j]=resval
    return res

def matrMult(a, b):
    "Multiplies two float matrix"
    l = len(a)
    c = len(b[0])
    common = len(a[0]) #len(a[0]) must be len(b)
    if(len(a[0])!=len(b)):
        print("Error in dimension")
        return []
    res = [[0.0]*c for i in range(l)]
    # print("dim res" + str(dimen(res)))
    # print("dim a" + str(dimen(a)))
    # print("dim b" + str(dimen(b)))
    for i in range(l):
        for j in range(c):
            resval = 0.0
            for k in range(common):
                resval +=  a[i][k] * b[k][j]
            res[i][j]=resval
    return res


