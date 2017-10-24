import numpy as np
from geomutils import add_coords
from distance import euclidean_dist


class Vector:
    def __init__(self, lst):
        self._coord = tuple(lst)

    def __add__(self, other):
        return add_coords(self, other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(tuple(x * other for x in self._coord))
        if len(self) != len(other):
            raise Exception('cannot multiply vectors of different dimensions')
        return np.dot(self._coord, other._coord)

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return euclidean_dist(self._coord)

    def __getitem__(self, i):
        return self._coord[i]

    def direction(self):
        d = abs(self)
        if d != 0:
            return self * (1 / d)

    def __len__(self):
        return len(self._coord)

    def __eq__(self, other):
        return self._coord == other._coord

    def __hash__(self):
        return hash(self._coord)

    def __str__(self):
        return str(self._coord)


if __name__ == "__main__":
    a = [1, 3]
    v = Vector(a)
    print(v * v)
    print(abs(v))
    print(v.direction())
    print(v[0], v[1])
    print(len(v))
    print(v - v)
    print(hash(v))
