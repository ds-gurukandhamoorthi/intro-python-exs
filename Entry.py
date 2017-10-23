class Entry:
    def __init__(self, date, opening, high, low, close, volume):
        self._date = date
        self._opening = opening
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume

    def close(self):
        return self._close

    def tuple(self):
        return (self._date, self._opening, self._high, self._low, self._close, self._volume)

    def __str__(self):
        return str(self.tuple())

if __name__ == "__main__":
    e = Entry('17/03/2016', 11,13,3,4,45345)
    print(e)

