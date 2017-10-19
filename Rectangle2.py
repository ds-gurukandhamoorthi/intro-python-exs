import matplotlib.patches as patches
import matplotlib.pyplot as plt
from geomutils import midpoint
class Rectangle2:

    def __init__(self, x, y, w, h):
        self._bottom_left = (x - w/2, y - h/2)
        self._top_right = (x + w/2, y + h/2)

    def width(self):
        return  self._top_right[0] - self._bottom_left[0]

    def height(self):
        return  self._top_right[1] - self._bottom_left[1]


    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return (self.width() + self.height())*2

    def contains_point(self, coord):
        x, y = coord
        xmin, ymin = self._bottom_left
        xmax, ymax = self._top_right
        return ( xmin <= x <= xmax) and (ymin <= y <= ymax)


    def center(self):
        return midpoint(self._bottom_left, self._top_right)

    def contains(self, other):
        return self.contains_point(other._bottom_left) and self.contains_point(other._top_right)

    def intersects(self, other):
        # hw1, hw2 = self._width/2, other._width/2
        # x1, x2 = self._x, other._x
        # hh1, hh2 = self._height/2, other._height/2
        # y1, y2 = self._y, other._y
        xmin, ymin = self._bottom_left
        xmax, ymax = self._top_right
        xmin_o, ymin_o = other._bottom_left
        xmax_o, ymax_o = other._top_right
        if max(xmin, xmin_o) <= min(xmax, xmax_o):
            if max(ymin, ymin_o) <= min(ymax, ymax_o):
                return True
        return False
            

    def get_patch(self):
        return patches.Rectangle(self._bottom_left, self.width(), self.height(), facecolor='none', edgecolor='black')

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
    r = Rectangle2(0,0, 6,6)
    s = Rectangle2(6,6,6,5)
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
