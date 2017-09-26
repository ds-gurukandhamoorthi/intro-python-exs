import argparse
import subprocess

from day_of import day_of
from array_utils import split_every

MONTH_NAMES=["","January", "February", "March", "April", "May", "June", "July", "August", "Septemeber", "October", "November", "December"]
DAY_ABBREVS=['Mo','Tu','We','Th','Fr','Sa','Su']

def is_leap_year(year):
    return (year % 4 == 0) and ( (year % 400 == 0) or (year % 100 != 0))

def nb_days_of_month(m, year):
    "one indexed"
    if month == 2 and is_leap_year(year):
        return 29
    return [0,31,28,31,30,31,30,31,31,30,31,30,31][m]

def month_name(n):
    "Zero indexed month name"
    return MONTH_NAMES[n]

def day_name(n):
    "Starting with monday"
    return DAY_ABBREVS[n]


def calendar(year, month):
    def get_start():
        res = day_of(1,month,year)-1
        if res < 0:
            return res + 7
        return res
    res = ""
    LEN = 20
    res += (month_name(month) + ' ' + str(year)).center(LEN) + '\n'
    res += ' '.join([day_name(n) for n in range(7)]) +'\n'
    res += lines(get_start(),nb_days_of_month(month, year))

    return res


def lines_array(offset=0, number_of_days=30):
    days = [0] * offset + list(range(1,number_of_days+1))
    return split_every(7,days)

def lines(day_of_start, nb_days):
    def daystr(n):
        if n > 0:
            return str(n).rjust(2)
        return ' ' * 2
    array = lines_array(day_of_start, nb_days)
    res = ''
    for row in array:
        res += ' '.join([daystr(val) for val in row]) +'\n'
    return res










    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='print calendar for the given month, year')
    parser.add_argument('year', type=int, help='year')
    parser.add_argument('month', type=int, help='month')
    args = parser.parse_args()
    year = args.year
    month = args.month
    print(calendar(year,month))
    print('system calendar')
    subprocess.run(['cal','-NMC', str(month), str(year)])
    # print(line(4,4,5))
    # print(line(1,1,5))
    # print(lines_array(4,30))
    # print(lines(4,30))




