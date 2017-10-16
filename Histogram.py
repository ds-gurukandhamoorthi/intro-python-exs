import matplotlib.pyplot as plt
from collections import Counter
class Histogram:

    def __init__(self, length):
        self._len = length
        self._freq_counts = Counter()

    def add_data_point(self, i):
        self._freq_counts[i] += 1

    def draw(self):
        arr = [0]* self._len
        for i,_ in enumerate(arr):
            arr[i] = self._freq_counts[i]
        print(arr)
        plt.hist(range(0,self._len),weights=arr)
        plt.show()

if __name__ == "__main__":
    h = Histogram(5)
    for v in [0,4,2,3,3,2]:
        h.add_data_point(v)
    h.draw()
        




