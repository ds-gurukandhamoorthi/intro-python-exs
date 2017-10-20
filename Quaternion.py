from distance import euclidean_dist
from geomutils import add_coords

class Quaternion:
    def __init__(self, a0, a1, a2, a3):
        self._values=(a0, a1, a2, a3)

    def __abs__(self):
        return euclidean_dist(self._values, (0, 0, 0, 0))

    def conjugate(self):
        a0, a1, a2, a3 = self._values
        return Quaternion(a0, -a1, a2, -a3)

    def inverse(self):
        a0, a1, a2, a3 = self._values
        magn = abs(self)
        return Quaternion(a0/magn, -a1/magn, -a2/magn, -a3/magn)
    
    def __add__(self, other):
        tupl = add_coords(self._values, other._values)
        return Quaternion(*tupl)
    
    def __mul__(self, other):
        a0, a1, a2, a3 = self._values
        b0, b1, b2, b3 = other._values
        n0 = a0*b0 - a1*b1  - a2*b2 - a3*b3
        n1 = a0*b1 + a1*b0  + a2*b3 - a3*b2
        n2 = a0*b2 - a1*b3  + a2*b0 + a3*b1
        n3 = a0*b3 + a1*b2  - a2*b1 + a3*b0
        return Quaternion(n0, n1, n2, n3)



    def __truediv__(self, other):
        return self * other.inverse()

    def __str__(self):
        return str(self._values)

if __name__ == "__main__":
    a = Quaternion(1, 2, 3, 4)
    print(abs(a))
    print(a.conjugate())
    print(a.inverse())
    print(a+a)
    print(a/a)



