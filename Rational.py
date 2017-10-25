from int_utils import gcd

class Rational:
    def __init__(self, num, den):
        if den == 0:
            raise Exception('Denominator must not be zero')
        sign = -1 if num * den < 0 else 1
        self._num = sign * abs(num//gcd(num,den))
        self._den = abs(den//gcd(num,den))

    def __add__(self, other):
        return Rational(self._num * other._den + other._num * self._den, self._den * other._den)

    def __mul__(self, other):
        return Rational(self._num * other._num, self._den * other._den)

    def __str__(self):
        return str(self._num) + '/' + str(self._den)

    def __neg__(self):
        return Rational(-self._num, self._den)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return Rational(abs(self._num), self._den)

if __name__ == "__main__":
    a = Rational(30,40)
    b = Rational(2,5)
    print(a+b)
    print(a-b)
    print(-a, -b)
    a = Rational(-3,4)
    b = Rational(3,-4)
    print(a,b)
    print(abs(a), abs(b))
    a = Rational(3,0)


