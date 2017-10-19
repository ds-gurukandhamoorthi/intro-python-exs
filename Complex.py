from math import sqrt
class Complex:
    def __init__(self, re, im):
        self._re = re
        self._im = im

    def re(self):
        return self._re

    def im(self):
        return self._im

    def __add__(self,other):
        return Complex(self.re() + other.re(), self.im() + other.im())

    def __mul__(self,other):
        return Complex(self.re() * other.re() - self.im() * other.im(), 
                self.re()*other.im() + self.im()*other.re())

    def __abs__(self):
        return sqrt(self.re()**2 +self.im()**2)

    def __str__(self):
        def is_int(x):
            return is_zero(x-int(x))
        def is_zero(x):
            return abs(x) < 10**-6
        def as_int(x):
            if is_int(x):
                return int(x)
            return x
        r, im = self.re() ,self.im()
        if is_zero(r): 
            if is_zero(im):
                return '0'
            return str(as_int(im)) + 'i'
        if is_zero(im):
            return str(as_int(r))
        sign = '+' if im >= 0 else '-'
        if is_zero(im-1) or is_zero(im+1):
            return str(as_int(r)) + sign + 'i'
        return str(as_int(r)) + sign + str(abs(as_int(im))) +'i'


    def __getattr__(self, attrname):
        if attrname == 'real':
            return self._re
        if attrname == 'imag':
            return self.im()


if __name__ == "__main__":
    c1 = Complex(5,0)
    print(abs(c1))
    c2 = Complex(3.0,1)
    print(c1, c2)
    c3=c2*c1
    print(c3.re(), c3.im())
    print(c1, c1.real, c1.imag)
    print(Complex(3,-1), Complex(3.0,-1.0), Complex(3,0), Complex(0,3), Complex(3.0,1.0), Complex(0,0))


