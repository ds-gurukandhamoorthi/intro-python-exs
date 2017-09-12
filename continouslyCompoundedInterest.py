import sys, math

amount = float(sys.argv[1])
roi = float(sys.argv[2]) / 100
years = int(sys.argv[3])

res = amount * math.e ** (roi * years)
print(res)
