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
    def increase_time(self, dt):
        forces = [Vector([0,0])] * len(self)
        for i, bod1 in enumerate(self):
            for j, bod2 in enumerate(self):
                if i != j:
                    forces[i] += bod1.force_from(bod2)
        for i in range(len(self)):
            self._bodies[i].move(forces[i], dt)
        return self

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
    dt = float(sys.argv[2])
    u = Universe(filename)
    while True:
        u.increase_time(dt)
        print(len(u))
        u.draw()


if __name__ == "__main__":
    main()
