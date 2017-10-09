from charge import Charge
from potential import total_potential
import sys

if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c1 = Charge((.51,.63), 21.3)
    c2 = Charge((.13,.94), 81.9)
    v1 = c1.potential_at((x,y))
    v2 = c2.potential_at((x,y))
    print('potential at', (x,y))
    print('due to', c1)
    print('and', c2)
    print('is %.2e' % (v1 + v2))
    print('%.2e' %total_potential((x,y),[c1,c2]))
