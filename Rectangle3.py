import matplotlib.patches as patches
import matplotlib.pyplot as plt
from geomutils import midpoint
from Interval import Interval
class Rectangle3:

    def __init__(self, x, y, w, h):
        self._xs = Interval(x - w/2, x + w/2)
        self._ys = Interval(y - h/2, y + h/2)

    def width(self):
        return  abs(self._xs)

    def height(self):
        return  abs(self._ys)

    def lower_corner(self):
        return (self._xs[0], self._ys[0])

    def upper_corner(self):
        return (self._xs[1], self._ys[1])


    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return (self.width() + self.height())*2

    def contains_point(self, coord):
        x, y = coord
        return x in self._xs and y in self._ys


    def contains(self, other):
        return other._xs in self._xs and other._ys in self._ys

    def intersects(self, other):
        return (other._xs).intersects(self._xs) and (other._ys).intersects(self._ys) 

    def get_patch(self):
        return patches.Rectangle(self.lower_corner(), self.width(), self.height(), facecolor='none', edgecolor='black')

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
        return str((self._bottom_left, self._top_right))


if __name__ == "__main__":
    r = Rectangle3(0,0, 6,6)
    s = Rectangle3(6,6,6,5)
    print(r.area())
    print(r.perimeter())
    print(r.contains_point((4,5)))
    print(r.contains_point((4,4)))
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
