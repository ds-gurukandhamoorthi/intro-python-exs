from ioutils import read_strings
import matplotlib.pyplot as plt
from math import log
import random
from collections import Counter

def leading_digit(s):
    return s.strip()[0]

def get_benford_dist(lines):
    freqs = Counter()
    count = 0
    for line in lines:
        dig = int(leading_digit(line))
        freqs[dig] += 1
        count += 1
    freqs_array = [freqs[k] for k in range(0,10)]
    freqs_array = [ f / count for f in freqs_array ]
    return freqs_array



def fake_benford():
    "Numbers from 1 to 1000"
    r = random.random()*3
    return str(10 ** r)



if __name__ == "__main__":
    lines = read_strings()
    freqs_array = get_benford_dist(lines)
    print(freqs_array)


    


    plt.plot(range(1,10),freqs_array[1:])


    theoritical_freq = [ log(1+1/d, 10) for d in range(1,10)]
    plt.plot(range(1,10), theoritical_freq)

    fake_lines = [fake_benford() for i in range(10000)]
    freqs_array = get_benford_dist(fake_lines)
    plt.plot(range(1,10),freqs_array[1:])


    plt.show()


    
   


