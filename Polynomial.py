from itertools import dropwhile
import toolz
from Rational import Rational
from horner import horner


class Polynomial:
    def __init__(self, coeffs, human_friendly=True):
        def drop_zeros_at_end(lst):
            return tuple(reversed(list(dropwhile(lambda x: x == 0, reversed(list(lst))))))
        if human_friendly:
            if list(coeffs)[0] == 0:
                raise Exception(
                    'A polynomial''s highest term''s coefficient must not be zero')
            self._coeffs = tuple(reversed(coeffs))
        else:
            # A polynomial's highest term's coefficient must not be zero
            self._coeffs = drop_zeros_at_end(coeffs)

    @property
    def degree(self):
        return len(self._coeffs) - 1

    # Basic Arithmetic
    def __add__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                return self
            return self + Polynomial((other,))
        n = max(self.degree, other.degree)
        tup = tuple(self[i] + other[i] for i in range(n + 1))
        return Polynomial(tup, human_friendly=False)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        tup = (-c for c in self)
        return Polynomial(tup, human_friendly=False)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self * Polynomial((other,))
        lst = [0] * (self.degree + 1 + other.degree + 1)
        for i, c1 in enumerate(self):
            for j, c2 in enumerate(other):
                lst[i + j] += c1 * c2
        return Polynomial(lst, human_friendly=False)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, n):
        if isinstance(n, int):
            if n < 0:
                return None
            if n == 0:
                return Polynomial((1,))
            if n == 1:
                return self
            return self * (self ** (n - 1))

    def __call__(self, x):
        # series = ( c * x ** i for i, c in enumerate(self))
        # return sum(series)
        if isinstance(x, (int, float, complex)):
            return horner(self._coeffs, x)
        if isinstance(x, Polynomial):
            return self.compose(x)

    # Operations specifically applied to polynomials
    def compose(self, other):
        if isinstance(other, Polynomial):
            series = (c * other ** i for i, c in enumerate(self))
            return sum(series)

    def differentiate(self):
        series = (c * i for i, c in enumerate(self) if i > 0)
        return Polynomial(tuple(series), human_friendly=False)

    def integrate(self):
        series = (0,) + tuple(c/(i+1) for i, c in enumerate(self))
        return Polynomial(series, human_friendly=False)

    def has_complex_coeffs(self):
        return any (isinstance(c, complex) for c in self)




    # Basic Comparisons
    def __eq__(self, other):
        return self._coeffs == other._coeffs

    # List like operations
    def __iter__(self):
        for c in self._coeffs:
            yield c

    def __getitem__(self, index):
        if isinstance(index, int) and index > self.degree:
            return 0
        return self._coeffs[index]

    # Basic Conversions
    def __str__(self):
        if self.has_complex_coeffs():
                return ' + '.join(str(c) + '×X^' + str(i)  for i, c in enumerate(self._coeffs))
        terms = []
        signs = []
        for i, c in enumerate(self):
            term = ''
            if c == 0:
                continue
            if c > 0:
                signs += ['+']
            elif c < 0:
                signs += ['-']
            else:
                signs += ['']

            if c not in (1, -1) or i == 0:
                term += str(abs(c))
            if i >= 1:
                term += 'x'
            if i >= 2:
                term += '^' + str(i)
            if term != '':
                terms += [term]
        terms, signs = list(reversed(terms)), list(reversed(signs))
        first_sign, signs = signs[0], (' ' + s + ' ' for s in signs[1:])
        if first_sign == '+':
            first_sign = ''
        return first_sign + ''.join(toolz.interleave([terms, signs]))


def test_sum():
    p = Polynomial((2, 5, 3, 1))
    q = Polynomial((6, 3, 7))
    assert (p+q)._coeffs == Polynomial((2, 11, 6, 8))._coeffs

if __name__ == "__main__":
    p = Polynomial((2, 5, 3, 1))
    print(p, p.differentiate(), p.differentiate().integrate(), sep = '|')
    q = Polynomial((6, 3, 7))
    print(q, p, p.compose(q), sep='|')
    print(p)
    print(p[0], p[1], p[3], p[4])
    print(p + q, (p + q)._coeffs)
    print(p, q, p - q, sep='|')
    print(-p)
    p = Polynomial((1, 5, 7))
    q = Polynomial((2, 3))
    print(p, q, p * q, sep='|')
    # q = Polynomial((Rational(1, 2), Rational(2, 3)))
    print(q, p, p.compose(q), sep='|')
    g = Polynomial((2,-4))
    h = Polynomial((-4,3))
    print(g(h), h(g))
    g_ = Polynomial((1, -2))
    print(g == (g_*2))
    print(g[1:])
    g = Polynomial((2+1j,-4+1j))
    h = Polynomial((-4+1j,3+1j))
    # g = Polynomial((Rational(4,3), Rational(5,2)))
    # h = Polynomial((Rational(14,17), Rational(11,3)))
    # g = Polynomial((0.3,0.4))
    # h = Polynomial((0.6,0.8))
    print((g+h)._coeffs)
    print((g*h)._coeffs)
    print(g.differentiate()._coeffs)
    print(g.integrate())
    print(g(1))
    print(g)
