from math import log
def rec_ln_fac(n):
    if n <= 1:
        return 0
    return rec_ln_fac(n-1) + log(n)

def ex233(n):
    print('called', n)
    if n <= 0:
        return
    print(n)
    ex233(n-2)
    ex233(n-3)
    print(n)

def ex234(n):
    if n <= 0:
        return ''
    return ex234(n-3) + str(n) + ex234(n-2) + str(n) 

def gcdlike(a,b):
    if b == 0:
        return a == 1
    return gcdlike(b, a%b)

def mystery(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return mystery(a*a, b//2)
    return mystery(a*a, b//2)*a

def rec_1(n):
    if n == 1:
        return 1
    return rec_1(n//2) + 1

def rec_sol1(n):
    return int(log(n,2)) + 1

def rec_2(n):
    if n == 1:
        return 1
    return 2*rec_2(n//2) + 1

def rec_sol2(n):
    return 2**(int(log(n,2)) + 1)-1

def rec_3(n):
    if n == 1:
        return 1
    return 2*rec_3(n//2) + n

def rec_sol3(n):
    m = int(log(n,2)) +1
    return m*2**(m-1)

def rec_4(n):
    if n == 1:
        return 1
    return 4*rec_4(n//2) + 3

def rec_sol4(n):
    m = int(log(n,2)) *  2  + 1
    return (2**(m))-1




if __name__ == "__main__":
    for i in range(10):
        print(i, rec_ln_fac(i))
    # ex233(6)
    
    for i in range(10):
        print(ex234(i))

    powers_of_two = [2**i for i in range(6)]
    print([(i,rec_1(i)) for i in powers_of_two])
    print([(i,rec_sol1(i)) for i in powers_of_two])
    print([(i,rec_2(i)) for i in powers_of_two])
    print([(i,rec_sol2(i)) for i in powers_of_two])
    print([(i,rec_3(i)) for i in powers_of_two])
    print([(i,rec_sol3(i)) for i in powers_of_two])
    print([(i,rec_4(i)) for i in powers_of_two])
    print([(i,rec_sol4(i)) for i in powers_of_two])

