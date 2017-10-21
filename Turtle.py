from math import cos, sin, radians
import matplotlib.collections
import matplotlib.pyplot as plt

class Turtle:

    def __init__(self, x0, y0, a0):
        self._x = x0
        self._y = y0
        self._a = radians(a0)
        self._lines = []

    def turn_left(self, angle):
        self._a += radians(angle)

    def go_forward(self, dist):
        x, y, a = self._x, self._y, self._a
        dx, dy = dist*cos(a), dist*sin(a)
        self._lines += [[[x,y], [dx+x,dy+y]]]
        self._x += dx
        self._y += dy

    def draw(self):
        lc = matplotlib.collections.LineCollection(self._lines)
        fig, ax = plt.subplots()
        ax.add_collection(lc)
        ax.axis('equal')
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        plt.axis('off')
        fig.savefig('tes.png')
        plt.show()

    def merge(self, other):
        self._lines += other._lines

if __name__ == "__main__":
    t = Turtle(0.5,0.5,90)
    t.go_forward(0.1)
    t.turn_left(90)
    t.go_forward(0.1)
    # print(t._lines)
    t.draw()



