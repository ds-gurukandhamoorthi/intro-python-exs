import sys
import re
import matplotlib.pyplot as plt
from Body import Body
from Vector import Vector


class Universe:
    def __init__(self, filename):
        with open(filename) as univ:
            lines = univ.read().split('\n')
            n = int(lines[0])
            self._radius = float(lines[1])
            self._bodies = [None] * n
            for i, line in enumerate(lines[2:n + 2]):
                x, y, vx, vy, m = [float(x)
                                   for x in re.split(r'\s+', line) if x != '']
                self._bodies[i] = Body(Vector([x, y]), Vector([vx, vy]), m)

    def __len__(self):
        return len(self._bodies)

    def __iter__(self):
        for body in self._bodies:
            yield body

    def draw(self):
        fig, ax = plt.subplots()
        # ax.axis('equal')
        r = self._radius
        ax.set_xlim(-r, r)
        ax.set_ylim(-r, r)
        for body in self:
            ax.add_patch(body.get_patch(radius=r/25))
        plt.savefig('tes.png')
        plt.show()


def main():
    filename = sys.argv[1]
    u = Universe(filename)
    print(len(u))
    u.draw()


if __name__ == "__main__":
    main()
