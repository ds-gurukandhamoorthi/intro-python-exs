import sys

def day_of(d, m, y):
    y0  = y- (14 - m ) //12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m + 12 *((14-m)//12) -2
    d0 = (d + x + (31*m0)//12) % 7
    return d0

if __name__ == "__main__":
    d = int(sys.argv[1])
    m = int(sys.argv[2])
    y = int(sys.argv[3])
    print(day_of(d,m,y))



