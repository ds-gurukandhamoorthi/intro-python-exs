import functools
from int_utils import gcd
from builtins import property


@functools.total_ordering
class Rational:
    def __init__(self, num, den):
        if den == 0:
            raise Exception('Denominator must not be zero')
        sign = -1 if num * den < 0 else 1
        self._num = sign * abs(num // gcd(num, den))
        self._den = abs(den // gcd(num, den))

    num = property(lambda o : o._num)
    den = property(lambda o : o._den)

    # BASIC ARITHMETIC
    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other, 1)
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int):
            return self * Rational(other, 1)
        return Rational(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Rational(-self.num, self.den)

    def __sub__(self, other):
        return self + (-other)

    def __pow__(self, n):
        if isinstance(n, int):
            if n >= 0:
                return Rational(self.num ** n, self.den ** n)

    def __truediv__(self, other):
        return ~self * other

    def __invert__(self):
        return Rational(self.den, self.num)

    def __abs__(self):
        return Rational(abs(self.num), self.den)

    # BASIC COMPARISONS
    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.den * other.num == self.num * other.den
        return float(self) == float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    # BASIC CONVERSIONS
    def __float__(self):
        return self.num / self.den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __iter__(self):
        yield from (self.num, self.den)


if __name__ == "__main__":
    a = Rational(30, 40)
    b = Rational(2, 5)
    print(a + b)
    print(a - b)
    print(-a, -b)
    a = Rational(-3, 4)
    b = Rational(3, -4)
    print(a, b)
    print(abs(a), abs(b))
    print(a < b, b <= a, tuple(a), tuple(b))
    print(a.num, a.den)
    # a = Rational(3,0)
