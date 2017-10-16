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
        if self.im() > 0:
            return str(self.re()) + '+' + str(self.im())+'i'
        if self.im() < 0:
            return str(self.re()) + '-' + str(-self.im())+'i'
        return str(self.re())

if __name__ == "__main__":
    c1 = Complex(5,0)
    print(abs(c1))
    c2 = Complex(3,0)
    c3=c2*c1
    print(c3.re(), c3.im())
    print(c1)


