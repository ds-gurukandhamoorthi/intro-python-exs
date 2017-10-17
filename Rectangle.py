class Rectangle:

    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width + self._height)*2

    def contains_point(self, coord):
        x, y = coord
        return (abs(x - self._x) <= self._width) and (abs(y - self._y) <= self._height)

    def corners(self):
        hlf_w = self._width/2
        hlf_h = self._height/2
        x, y = self._x, self._y
        return ((x + hlf_w, y - hlf_h),
                (x + hlf_w, y + hlf_h),
                (x - hlf_w, y - hlf_h),
                (x - hlf_w, y + hlf_h))


if __name__ == "__main__":
    r = Rectangle(0,0, 4,5)
    print(r.area())
    print(r.perimeter())
    print(r.contains_point((4,5)))
    print(r.contains_point((4,4)))
    print(r.corners())
