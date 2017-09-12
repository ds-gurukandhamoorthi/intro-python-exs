import sys
maxval = int(sys.argv[1])
power = 1

while power * 2 <= maxval:
    power *= 2
print(power)
