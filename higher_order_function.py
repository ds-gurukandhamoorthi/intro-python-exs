import numpy as np


def square(x):
    return x * x


def integrate(f, a, b, n=1000):
    dx = (b - a) / n
    xs = np.linspace(a + dx / 2, b + dx / 2, n + 1)[0:n]
    return sum(dx * f(x) for x in xs)


def integrate_(f, a, b, n=1000):
    dx = 1.0 * (b - a) / n
    series = (dx * f(a + (i + 0.5) * dx) for i in range(n))
    return sum(series)


if __name__ == "__main__":
    print(integrate(square, 2, 3, 1000))
    print(integrate_(square, 2, 3, 1000))
