class SparseVector:
    def __init__(self):
        self._coords = {}
        self._dim = 0

    def __setitem__(self, index, val):
        self._coords[index] = val
        self._dim = max(self._dim, index + 1)

    def __getitem__(self, index):
        if index in self._coords:
            return self._coords[index]
        return 0

    def items(self):
        yield from self._coords.items()

    def __iter__(self):
        for i in range(self._dim):
            yield self._coords.get(i,0)


    def __str__(self):
        return str(tuple(self))

    def __add__(self, other):
        res = SparseVector()
        for i, val in self.items():
            res[i] = val
        for i, val in other.items():
            res[i] += val
        return res

    def dot(self, other):
        return sum(val1 * val2 for val1, val2 in zip(self, other))



def main():
    v = SparseVector()
    v[1] = 1
    v[0] = 2
    u = SparseVector()
    u[1] = 1
    print(v, u)
    for k, val in v.items():
        print(k, val)
    print(u+v)
    print(u.dot(v))


if __name__ == "__main__":
    main()
