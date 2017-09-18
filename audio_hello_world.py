import sys
sys.path.append('../')
import stdaudio
import math

SPS = 44100
hz = 440.00
duration = 10.0

n = int(SPS * duration)
a = [0.0] * (n+1)
for i in range(n+1):
    a[i] = math.sin(2.0 * math.pi * hz / SPS)

stdaudio.playSamples(a)
stdaudio.wait()
