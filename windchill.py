import sys, math

t = float(sys.argv[1])
v = float(sys.argv[2])
if abs(t) > 50:
    print("error : temperature greater than 50 in absolute value")
elif not( 3 < v < 120):
    print("error : windspeed not in range [3, 120]")
else:
    windchill = 35.74+0.6215*t+(0.4275*t -35.75)*v**.16
    print(windchill)
