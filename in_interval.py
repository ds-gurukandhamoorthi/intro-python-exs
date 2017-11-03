def in_interval(string, n):
    a, b = string.split('-')
    a, b = int(a), int(b)
    return n in range(a, b+1)

if __name__ == "__main__":
    intervals = ['1643-2033','5532-7643', '8999-10332', '5666653-5669321']
    n = 9122
    for intrvl in intervals:
        if in_interval(intrvl, n):
            print(intrvl)
    # print(in_interval('1643-2033', 8122))
    # print(in_interval('1643-2033', 2034))

