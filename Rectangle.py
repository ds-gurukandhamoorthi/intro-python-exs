import matplotlib.patches as patches
import matplotlib.pyplot as plt
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

    def center(self):
        return (self._x, self._y)

    def contains(self, other):
        return all ( self.contains_point(corner) for corner in other.corners())

    def intersect(self, other):
        hw1, hw2 = self._width/2, other._width/2
        x1, x2 = self._x, other._x
        if x1 + hw1 >= x2 - hw2 or x2 + hw2 >= x1 - hw1:
            return True
        hh1, hh2 = self._height/2, other._height/2
        y1, y2 = self._y, other._y
        if y1 + hh1 >= y2 - hh2 or y2 + hh2 >= x2 - hh2:
            return True
        return False

    def get_patch(self):
        return patches.Rectangle(self.center(), self._width, self._height, facecolor='none', edgecolor='black')

    def draw(self):
        rect = self.get_patch()
        fig, ax = plt.subplots()
        ax.axis('equal')
        ax.add_patch(rect)
        ax.set_xlim([0,10])
        ax.set_ylim([0,10])
        plt.axis('off')
        fig.savefig('tes.png')
        plt.show()





if __name__ == "__main__":
    r = Rectangle(0,0, 4,5)
    s = Rectangle(6,6,4,4)
    print(r.area())
    print(r.perimeter())
    print(r.contains_point((4,5)))
    print(r.contains_point((4,4)))
    print(r.corners())
    print(r.contains(s))
    print(r.intersect(s))
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.add_patch(r.get_patch())
    ax.add_patch(s.get_patch())
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])
    plt.axis('off')
    fig.savefig('tes.png')
    plt.show()
