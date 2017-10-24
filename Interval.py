class Interval:
    def __init__(self, left, right):
        assert left <= right
        self._left = left
        self._right = right

    def __contains__(self, other):
        if isinstance(other, (int, float)):
            return self._left <= other <= self._right
        return other._left >= self._left and other._right <= self._right

    def __str__(self):
        return '['+str(self._left) + ' '+ str(self._right) +']'

    def __abs__(self):
        return self._right - self._left

    def __and__(self, other):
        lft = max(self._left, other._left)
        rgt = min(self._right, other._right)
        if lft <= rgt:
            return Interval(lft, rgt)
        return None

    def __getitem__(self, i):
        if i == 0:
            return self._left
        if i == 1:
            return self._right

    def intersects(self, other):
        return (self & other) is not None

if __name__ == "__main__":
    a = Interval(3, 4)
    b = Interval(3.5, 4.8)
    print(b in a)
    print(a, b)
    print(a&b)
    print(a.intersects(b))
    print(abs(a), abs(b))
    print(a[0], a[1], a)
