import functools
import datetime
from day_of import day_of
from calend_utils import as_days


@functools.total_ordering
class Date:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def __sub__(self, other):
        d1 = datetime.date(*tuple(self))
        d2 = datetime.date(*tuple(other))
        return (d1 - d2).days

    def day_of(self):
        return day_of(self._day, self._month, self._year)

    def sub(self, other):
        return int(self) - int(other)

    def __iter__(self):
        for x in (self._year, self._month, self._day):
            yield x

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __le__(self, other):
        return tuple(self) < tuple(other)

    def __str__(self):
        return '%02d/%02d/%04d' % tuple(self)

    def __int__(self):
        return as_days(*tuple(self))


if __name__ == "__main__":
    d1 = Date(1983, 1, 3)
    d2 = Date(2017, 10, 26)
    # print(d1, tuple(d1), d1 > d2, min(d1,d2), d1-d2)
    print(d1 - d2)
    print(d1.day_of())
    print(d1.sub(d2))
    print(int(d1))
