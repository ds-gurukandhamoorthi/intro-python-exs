import random
from tuple_utils import swp

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

def rand(m,n):
    return create_matrix(m, n, lambda _x,_y: random.random())

def rand_bool_matr(n, prob=0.5):
    return create_matrix(n, n, lambda _x,_y: random.random()<prob)


def identity(n):
    return create_matrix(n, n, lambda l,c: 1 if l==c else 0 )

def dot(vec1, vec2):
    return sum((a * b for a, b in zip(vec1, vec2)))

def transpose(matr):
    def trnsp(i,j):
        return matr[j][i]
    return create_matrix(*swp(dimen(matr)), trnsp)

def add(matr1, matr2):
    def value_at(i,j):
        return matr1[i][j] + matr2[i][j]
    return create_matrix(*dimen(matr1), value_at)

def sub(matr1, matr2):
    def value_at(i,j):
        return matr1[i][j] - matr2[i][j]
    return create_matrix(*dimen(matr1), value_at)

def create_matrix(m, n, func):
    res = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = func(i,j)
    return res

def multiplyMV(m,v):
    return transpose(matrMult( m, transpose([v])))[0]

def multiplyVM(v, m):
    return matrMult([v], m)[0]


            




