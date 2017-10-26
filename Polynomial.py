class Polynomial:
    def __init__(self, coeffs, human_friendly=True):
        if human_friendly:
            self._coeffs = tuple(reversed(coeffs))
        else:
            self._coeffs = tuple(coeffs)

    @property
    def degree(self):
        return len(self._coeffs) - 1

    def __iter__(self):
        for c in self._coeffs:
            yield c

    def __getitem__(self, index):
        if index > self.degree:
            return 0
        return self._coeffs[index]

    def __add__(self, other):
        n = max(self.degree, other.degree)
        tup = tuple(self[i] + other[i] for i in range(n+1))
        return Polynomial(tup, human_friendly=False)

    def __neg__(self):
        tup = (-c for c in self)
        return Polynomial(tup, human_friendly=False)

    def __str__(self):
        terms = []
        for i, c in enumerate(self):
            term = ''
            if c == 0:
                continue
            if c not in (1,-1):
                term += str(c)
            if i >= 1:
                term += 'x'
            if i >= 2:
                term += '^' + str(i)
            if term != '':
                terms += [term]
        return ' + '.join(reversed(terms))


if __name__ == "__main__":
    p = Polynomial((1, 5, 3, 7))
    q = Polynomial(( 5, 3, 7))
    print(p, p.degree)
    print(p[0], p[1], p[3], p[4])
    print(p+q)
    print(-p)
