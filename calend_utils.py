MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June",
               "July", "August", "Septemeber", "October", "November", "December"]
DAY_ABBREVS = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']


def month_name(n):
    "Zero indexed month name"
    return MONTH_NAMES[n]


def day_name(n):
    "Starting with monday"
    return DAY_ABBREVS[n]


def is_leap_year(year):
    return (year % 4 == 0) and ((year % 400 == 0) or (year % 100 != 0))


def nb_days_of_month(month, year):
    "one indexed"
    if month == 2 and is_leap_year(year):
        return 29
    return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]


def nb_days_in_year(year):
    return 366 if is_leap_year(year) else 365

def as_days(year, month, day):
    res = sum(nb_days_in_year(y) for y in range(year))
    res += sum(nb_days_of_month(m, year) for m in range(1, month))
    res += day
    return res


