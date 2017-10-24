import numpy as np
from geomutils import add_coords
from distance import euclidean_dist

class Vector:
    def __init__(self, lst):
        self._coord = tuple(lst)

    def __add__(self, other):
        return add_coords(self, other)

    def __mul__(self, other):
        if type(other) in (type(3), type(3.1)):
            return Vector(tuple(x * other for x in self._coord))
        return np.dot(self._coord, other._coord)

    def __abs__(self):
        return euclidean_dist(self._coord)

    def direction(self):
        d = abs(self)
        if d != 0:
            return self * (1/d)

    def __str__(self):
        return str(self._coord)



if __name__ == "__main__":
    a = [1,3] 
    v = Vector(a)
    print(v*v)
    print(abs(v))
    print(v.direction())

