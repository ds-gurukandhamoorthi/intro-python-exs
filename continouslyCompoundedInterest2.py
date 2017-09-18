import sys, math

amount = float(sys.argv[1])
roi = float(sys.argv[2]) / 100
years = int(sys.argv[3])

prev = amount
for i in range(1,years+1):
    res = amount * math.e ** (roi * i)
    print('%3d' % i,  '%8.2f' % prev, '%8.2f' %  res)
    prev = res
