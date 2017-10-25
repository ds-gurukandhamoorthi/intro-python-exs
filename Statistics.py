from math import sqrt
class Statistics:
    def __init__(self, points):
        self._points = points[:]

    def __iadd__(self, point):
        if isinstance(point, (int, float)):
            self._points += [point]
        else:
            self._points += point
        return self

    def __str__(self):
        return str(self._points)

    def __len__(self):
        return len(self._points)

    def __iter__(self):
        for point in self._points:
            yield point


    def mean(self):
        return sum(self) / len(self)

    def variance(self):
        m = self.mean()
        return sum((x - m)**2 for x in self._points) /len(self)

    def std_deviation(self):
        return sqrt(self.variance())


if __name__ == "__main__":
    b= [3,4,5]
    a = Statistics(b)
    print(a)
    a += 6
    print(a)
    a += [5,6]
    print(a, sum(a), a.mean(), a.variance(), a.std_deviation())
    a = Statistics([1,2,3])
    print(a, sum(a), a.mean(), a.variance(), a.std_deviation())
    print(sum(a))


    
    
