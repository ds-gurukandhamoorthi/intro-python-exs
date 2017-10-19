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
        return (abs(x - self._x) <= self._width/2) and (abs(y - self._y) <= self._height/2)

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

    def intersects(self, other):
        hw1, hw2 = self._width/2, other._width/2
        x1, x2 = self._x, other._x
        hh1, hh2 = self._height/2, other._height/2
        y1, y2 = self._y, other._y
        if max(x1 - hw1, x2 - hw2) <= min(x1 + hw1, x2 + hw2):
            if max(y1 - hh1, y2 - hh2) <= min(y1 + hh1, y2 + hh2):
                return True
        return False
            

    def get_patch(self):
        lower_left = (self._x - self._width/2, self._y - self._height/2)
        return patches.Rectangle(lower_left, self._width, self._height, facecolor='none', edgecolor='black')

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

    def __str__(self):
        return str((self._x, self._y, self._width, self._height))

    def __contains__(self, coord):
        return self.contains_point(coord)





if __name__ == "__main__":
    r = Rectangle(0,0, 6,6)
    s = Rectangle(6,6,6,5)
    print(r.area())
    print(r.perimeter())
    print(r.contains_point((4,5)))
    print('overloaded', (4,5) in r)
    print(r.contains_point((4,4)))
    print(r.corners())
    print(r.contains(s))
    print(r.intersects(r))
    print(r.intersects(s))
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.add_patch(r.get_patch())
    ax.add_patch(s.get_patch())
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])
    plt.axis('off')
    fig.savefig('tes.png')
    plt.show()
