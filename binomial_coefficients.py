def pascal_triangle_row(n):
    if n == 1:
        return [1]
    res = [1] * n
    prev = pascal_triangle_row(n-1)
    for i in range(1, n-1):
        res[i] = prev[i-1] + prev[i]
    return res

def binomial_coefficients(n):
    res = []
    pasc_row = pascal_triangle_row(n)
    total = sum(pasc_row) 
    #print(total, 2**(n-1)) This is a property we can use to optimize a little
    for val in pasc_row:
        res += [val/total]
    return res

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
