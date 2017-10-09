from distance import euclideanDist
import sys
class Charge:
    def __init__(self, coord, q):
        self._coord=coord
        self._q = q

    def potential_at(self, coord):
        COULOMB=8.99*10**9 #N m²/C²
        r = euclideanDist(self._coord, coord)
        q = self._q
        if r == 0:
            return float('inf') if q >= 0 else float('-inf')
        return (COULOMB * q)/r

    def __str__(self):
        res = '%f at %s' % (self._q, self._coord)
        return res
if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c = Charge((.51,.63), 21.3)
    print(c)
    print(c.potential_at((x,y)))



