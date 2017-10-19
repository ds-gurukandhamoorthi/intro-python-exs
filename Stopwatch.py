import time

class Stopwatch:

    def __init__(self):
        self._started = time.time()
        self._prev_total_elapsed = 0

    def get_elapsed(self):
        return time.time()-self._started + self._prev_total_elapsed

    def pause(self):
        self._prev_total_elapsed += time.time()-self._started

    def restart(self):
        self._started = time.time()

if __name__ == "__main__":
    a = Stopwatch()
    time.sleep(2)
    a.pause()
    time.sleep(4)
    a.restart()
    time.sleep(3)
    print(a.get_elapsed())
