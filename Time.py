import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __iter__(self):
        yield from (self._hours, self._minutes, self._seconds)

    def __str__(self):
        return '%s:%s:%s' % tuple(self)

    def now():
        dt = datetime.datetime.now().time()
        return dt.hour, dt.minute, dt.second


if __name__ == "__main__":
    h = Time(4, 10, 23)
    print(h, tuple(h), Time.now())
