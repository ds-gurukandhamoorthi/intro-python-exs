import sys
import functools
from distance import euclidean_dist


@functools.total_ordering
class Charge:
    def __init__(self, coord, charge):
        self._coord = coord
        self._charge = charge

    def potential_at(self, coord):
        COULOMB = 8.99 * 10**9  # N m²/C²
        r = euclidean_dist(self._coord, coord)
        q = self._charge
        if r == 0:
            return float('inf') if q >= 0 else float('-inf')
        return (COULOMB * q) / r

    def increase_charge(self, charge):
        self._charge += charge

    def __iadd__(self, charge):
        self.increase_charge(charge)
        return self

    def __str__(self):
        res = '%f at %s' % (self._charge, self._coord)
        return res

    def __lt__(self, other):
        return self._charge < other._charge

    def __eq__(self, other):
        return self._charge == other._charge


if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c = Charge((.51, .63), 21.3)
    d = Charge((.51, .63), 21.3)
    print(c < d, c <= d, c == d, c >= d, c != d, c > d)
    c += .2
    print(c)
    print(c.potential_at((x, y)))
