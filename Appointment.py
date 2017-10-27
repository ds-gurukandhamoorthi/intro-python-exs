import datetime
import functools


@functools.total_ordering
class Appointment:
    def __init__(self, start, end, title, details):
        self._start = start
        self._end = end
        self._title = title
        self._details = details

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __eq__(self, other):
        return (self.start, self.end) == (other.start, other.end)

    def __lt__(self, other):
        return self.start < other.start

    def clashes_with(self, other):
        if self.start < other.start < self.end:
            return True
        if self.start < other.end < self.end:
            return True
        return False

    def __str__(self):
        strt = self.start.strftime('%d/%m/%Y %H:%m:%S')
        end = self.end.strftime('%d/%m/%Y %H:%m:%S')
        return strt + ' -- ' + end + ' : ' + self._title

def main():
    strt = datetime.datetime(2017, 10, 27, 10, 30, 12)
    end = datetime.datetime(2017, 10, 27, 11, 30, 12)
    a = Appointment(strt, end, 'Appnt1', 'an example of an appointment')
    strt = datetime.datetime(2017, 10, 27, 11, 30, 12)
    end = datetime.datetime(2017, 10, 27, 12, 30, 12)
    b = Appointment(strt, end, 'Appnt2', 'another example of an appointment')
    print(a.clashes_with(b), a < b)

if __name__ == "__main__":
    main()
