import matplotlib.patches as patches
import matplotlib.pyplot as plt
import scipy.constants
from Vector import Vector


class Body:
    def __init__(self, position, velocity, mass):
        self._position = position
        self._velocity = velocity
        self._mass = mass

    def move(self, force, dt):  # dt = time elapsed
        acceleration = force / self._mass
        # self._velocity = self._velocity + acceleration * dt
        self._velocity += acceleration * dt
        self._position += self._velocity * dt

    def force_from(self, other):
        G = scipy.constants.G
        delta = other._position - self._position
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist ** 2)
        return magnitude * delta.direction()

    def get_patch(self, radius=0.2):
        x, y = self._position
        return patches.Circle((x, y), radius, facecolor='black')


def main():
    pos = Vector([3, 4])
    velocity = Vector([.5, .1])
    body = Body(pos, velocity, 5)
    body.move(Vector([.2, .1]), 2)
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.add_patch(body.get_patch())
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    plt.savefig('tes.png')
    plt.show()


if __name__ == "__main__":
    main()
