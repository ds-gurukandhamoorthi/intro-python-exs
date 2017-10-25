import sys
from numpy.random import choice


class Counter:
    def __init__(self, name, max_count):
        if max_count <= 0:
            raise Exception('max count of a counter must be at least 1')
        self._name = name
        self._max_count = max_count
        self._counter = 0

    def increment(self):
        assert self._counter >= 0, 'Negative count detected!'
        if self._counter < self._max_count:
            self._counter += 1
        else:
            print('error Counter max')

    def value(self):
        return self._counter

    def __str__(self):
        return self._name + ': ' + str(self._counter)

    def __eq__(self, other):
        return self._counter == other._counter

    def __ne__(self, other):
        return self._counter != other._counter


if __name__ == "__main__":
    # a = Counter('ewrw', 10)
    # a.increment()
    # print(a)
    # a._counter = -1
    # a.increment()
    # print(a)
    def coin_toss(prob=0.5):
        probs = [prob, 1 - prob]
        return choice(range(2), size=1, p=probs)[0]

    n = int(sys.argv[1])
    p = float(sys.argv[2])
    head = Counter('heads', n)
    tail = Counter('tails', n)
    for i in range(n):
        if coin_toss(p) == 0:
            head.increment()
        else:
            tail.increment()
    print(head, tail, head != tail)
    a = Counter('ewrwer', 1)
