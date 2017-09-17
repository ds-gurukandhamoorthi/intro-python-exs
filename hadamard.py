import math
import printBoolArray
def hadamard(n):
    "Hadamard matrix of n with n a power of 2"
    if n == 1:
        return [[True]]
    hn_1 = hadamard(int(math.sqrt(n)))
    inv_hn_1 = invBoolMatr(hn_1)
    row1 = hstack(hn_1,hn_1)
    row2 = hstack(hn_1,inv_hn_1)
    return vstack(row1, row2)



def hstack(ma, mb):
    res = []
    for rowa, rowb in zip(ma,mb):
        res += [rowa + rowb]
    return res

def vstack(ma, mb):
    res = []
    for row in ma:
        res += [row]
    for row in mb:
        res += [row]
    return res

def mapFuncMatrix(func, m):
    res =[]
    for row in m:
        res += [[func(x) for x in row]]
    return res


def invBoolMatr(matr):
    def funcNot(x):
        return not x
    return mapFuncMatrix(funcNot, matr)

        

if __name__ == "__main__":
    # print(invBoolMatr([[True,False],[False,True]]))
    print("h1",hadamard(1))
    print("h2",hadamard(2))
    print("h4",hadamard(4))

    printBoolArray.printMatrix(hadamard(1),'T','F')
    printBoolArray.printMatrix(hadamard(2),'T','F')
    printBoolArray.printMatrix(hadamard(4),'T','F')
    printBoolArray.printMatrix(hadamard(16),'T','F')
