import sys
import pandas as pd
import matplotlib.pyplot as plt
from Entry import Entry
from array_utils import moving_avg

class Table:
    def __init__(self, filename):
        df = pd.read_csv(filename, index_col=False)
        nb_rows = df.shape[0]
        self._entries = [None] * nb_rows
        for i in range(nb_rows):
            dt = df.loc[i, 'Date']
            op = df.loc[i, 'Open']
            hi = df.loc[i, 'High']
            lo = df.loc[i, 'Low']
            cl = df.loc[i, 'Close']
            vol = df.loc[i, 'Volume']
            entry = Entry(dt, op, hi, lo, cl, vol)
            self._entries[i] = entry

    def __getitem__(self, key):
        return self._entries[key]

    def plot(self):
        values = [e.close() for e in self._entries]
        ma = moving_avg(values, 50)
        plt.plot(values)
        plt.plot(ma)
        plt.show()

if __name__ == "__main__":
    filename = sys.argv[1]
    t = Table(filename)
    print(t[0])
    t.plot()




