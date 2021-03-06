import math
from operator import mul
from functools import reduce
from funcy import ilen, any


def odd(n):
    return (n % 2) == 1


def even(n):
    return (n % 2) == 0


def gcd(a, b):
    "Calculates the greatest common divisor of two numbers"
    if (a, b) == (0, 0):
        raise Exception('Gcd of 0 and 0 is undefined')
    if a == 0:
        return b
    if b == 0:
        return a
    a, b = abs(a), abs(b)
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def bezout(a, b):
    if a % b == 0:
        return (b, 0, 1)
    (d, p, q) = bezout(b, a % b)
    return (d, q, p - (a // b) * q)


def common_multiple(a, b):
    "Calculate the common multiple of two numbers"
    a, b = abs(a), abs(b)
    return (a * b) // gcd(a, b)


def is_relatively_prime(a, b):
    return gcd(a, b) == 1


def totatives(n):
    return [i for i in range(1, n + 1) if is_relatively_prime(i, n)]


def totient(n):
    "Euler's totient : number of integers less than n and relatively prime with n"
    return len(totatives(n))


def find_one_strict_factor(n):
    if n % 2 == 0:
        return True
    divises_n = lambda i : n % i == 0
    return any(divises_n, range(3, int(math.sqrt(n)) + 1, 2))


def is_prime(n):
    if n <= 1:
        return False
    if n in {2, 3}:
        return True
    return not find_one_strict_factor(n)


def count_primes(n):
    nbPrimes = 1 if n >= 2 else 0
    return nbPrimes + ilen(filter(is_prime, range(3, n, 2)))


def prime_factors(n):
    n = abs(n)
    res = []
    d = 2
    while n > 1:
        if n % d == 0:
            res += [d]
            n /= d
        else:
            d += 1
    return res


def positive_factors(n):
    res = [i for i in range(2, int(n / 2 + 1)) if n % i == 0]
    return [1] + res + [n]


def product(array):
    return reduce(mul, array, 1)


if __name__ == "__main__":
    from rle import rle
    for i in range(2, 100):
        fac = prime_factors(i)
        count_fac = rle(fac)
        # ex: 96 = 2*5 *3  2  can be 0 times to 5 times : 6 possib  3 can be 0 or 1 so 2 possib 6 * 2 = 18 possib : 18 factors
        nb_pos_fac = product(count + 1 for count, n in count_fac)
        print(i)
        assert len(positive_factors(i)) == nb_pos_fac
        print(i, fac, positive_factors(i))
        assert i == product(fac)
    print(gcd(1440, 408))
    print(bezout(42, 12))
