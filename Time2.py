class Time:
    def __init__(self, hours, minutes, seconds):
        self._seconds_elapsed = hours * 3600 + minutes * \
            60 + seconds  # seconds elapsed since midnight

    @property
    def hour(self):
        return self._seconds_elapsed // 3600

    @property
    def minute(self):
        h = self.hour
        return (self._seconds_elapsed - (h * 3600)) // 60

    @property
    def second(self):
        h, m = self.hour, self.minute
        return self._seconds_elapsed - (h * 3600) - (m * 60)

    def __iter__(self):
        yield from (self.hour, self.minute, self.second)

    def __str__(self):
        return '%s:%s:%s' % tuple(self)


def main():
    h = Time(4, 10, 23)
    print(h.hour, h.minute, h.second)
    print(h, tuple(h))


if __name__ == "__main__":
    main()
