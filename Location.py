from math import radians, sin, cos, acos, degrees
import sys
class Location:

    def __init__(self, lat, lon):
        self._lat = radians(lat)
        self._lon = radians(lon)

    def distance(self, other):
        x1, y1 = self._lat, self._lon
        x2, y2 = other._lat, other._lon
        angle1 = acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
        return degrees(angle1) * 60 #nautical miles
if __name__ == "__main__":
    lat1 = float(sys.argv[1])
    lon1 = float(sys.argv[2])
    lat2 = float(sys.argv[3])
    lon2 = float(sys.argv[4])

    location1 = Location(lat1, lon1)
    location2 = Location(lat2, lon2)
    print(location2.distance(location1))
    print(location1.distance(location2))





