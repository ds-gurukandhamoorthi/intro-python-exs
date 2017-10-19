from distance import euclidean_dist
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance_to(self, other):
        return euclidean_dist((self._x, self._y), (other._x, other._y))

    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'

if __name__ == "__main__":
    a= Point(3,4)
    o = Point(0,1)
    print(a.distance_to(o))
    print(a, o)
