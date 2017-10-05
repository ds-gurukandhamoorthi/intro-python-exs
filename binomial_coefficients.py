from array_utils import normalize
from printBoolArray import show_ragged_matr
def pascal_triangle_row(n):
    if n == 1:
        return [1]
    prev = pascal_triangle_row(n-1)
    return [1] + [prev[i-1] + prev[i] for i in range(1, n-1)] + [1]

def binomial_coefficients(n):
    return normalize(pascal_triangle_row(n))

def pascal_triangle(n):
    res =[[1]]
    for i in range(1,n):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = res[i-1][j-1] + res[i-1][j]
        res += [row]
    return res

def binom_distrib(n):
    res = []
    pascal_triang = pascal_triangle(n)
    for i,row in enumerate(pascal_triang):
        res += [[ val / 2**i for val in row ]]
    return res

def oddity_pascal_triangle(n):
    def odd(n):
        return n%2 == 1
    res = []
    pascal = pascal_triangle(n)
    for row in pascal:
        res += [[odd(i) for i in row]]
    return res






    

if __name__ == "__main__":
    print(pascal_triangle_row(4))
    print(binomial_coefficients(2))
    print(binomial_coefficients(3))
    print(binomial_coefficients(4))
    print(binomial_coefficients(5))
    print(binom_distrib(5))
    print(pascal_triangle(1))
    print(pascal_triangle(2))
    print(pascal_triangle(3))
    print(pascal_triangle(4))
    print(pascal_triangle(5))
    print(oddity_pascal_triangle(5))
    show_ragged_matr(oddity_pascal_triangle(50))
