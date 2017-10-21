import matplotlib.pyplot as plt
class Data:
    def __init__(self, n):
        self._n = n
        self._values = [[] for i in range(n)]

    def __getitem__(self, key):
        return self._values[key]

    def __iadd__(self, other):
        if type(other) == type((1,3.1)):
            i, val = other
            if  0 <= i < self._n:
                self._values[i] += [val]
            else:
                print('Error in index')
        return self

    def get_points(self):
        res = []
        for i, vals in enumerate(self._values):
            for v in vals:
                res += [(i,v)]
        return res

    def plot(self):
        pts = self.get_points()
        xs = [x for x,y in pts]
        ys = [y for x,y in pts]
        plt.boxplot(self._values)
        plt.scatter(xs,ys)
        plt.show()
        
        

    def __str__(self):
        return str(self._values)

if __name__ == "__main__":
    dt = Data(3)
    print(dt)
    dt+=(0,5)
    dt+=(0,9)
    dt+=(1,9)
    print(dt)
    print(dt.get_points())
    dt.plot()

            



