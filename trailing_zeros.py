from math import log
def trailing_zeros_factorial(n):
    max_power_5 = int(log(n,5))
    res = 0
    for i in range(1, max_power_5 + 1):
        res += n // 5 ** i
    return res

if __name__ == "__main__":
    for n in (23,101, 777, 1000, 4617):
        print(n, trailing_zeros_factorial(n))


