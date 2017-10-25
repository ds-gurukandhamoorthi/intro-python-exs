from Vector import Vector
class Particle:
    def __init__(self, position, velocity, mass):
        if len(position) != 3 or len(velocity) != 3:
            raise Exception('Not a three-dimensional particle')
        self._position = Vector(position)
        self._velocity = Vector(velocity)
        self._mass = mass

    def __str__(self):
        return str(self._position) + str(self._velocity)

    def __iter__(self):
        for coord, veloc in zip(self._position, self._velocity):
            yield coord, veloc

    def kinetic_energy(self):
        return 0.5 * self._mass * sum(v**2 for v in self._velocity)

    def momentum(self):
        return self._velocity * self._mass


if __name__ == "__main__":
    p = Particle((1, 2, 3), (3, 4, 5), 50)
    print(p)
    print(p.momentum())
    for c, v in p:
        print(c, v)
