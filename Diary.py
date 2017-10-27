import datetime
from Appointment import Appointment


class Diary:
    def __init__(self, name):
        self._name = name
        self._list_appointments = []

    def __iter__(self):
        for app in self._list_appointments:
            yield app

    def __len__(self):
        return len(self._list_appointments)

    def __iadd__(self, appointment):
        if all(not prev_committment.clashes_with(appointment) for prev_committment in self):
            self._list_appointments += [appointment]
            return self
        print('The appointment you want to add clashes with one previous commitment')
        return self

    def __str__(self):
        res = self._name + ':\n'
        for app in self:
            res += str(app) + '\n'
        return res


def main():
    strt = datetime.datetime(2017, 10, 27, 10, 30, 12)
    end = datetime.datetime(2017, 10, 27, 11, 30, 12)
    a = Appointment(strt, end, 'Appnt1', 'an example of an appointment')
    strt = datetime.datetime(2017, 10, 27, 11, 29, 12)
    end = datetime.datetime(2017, 10, 27, 12, 30, 12)
    b = Appointment(strt, end, 'Appnt2', 'another example of an appointment')
    d = Diary('guru''s')
    print(d)
    d += a
    d += b
    print(d)


if __name__ == "__main__":
    main()
