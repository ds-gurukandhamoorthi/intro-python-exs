import time

class Stopwatch:

    def __init__(self):
        self._started = time.time()

    def get_elapsed(self):
        return time.time()-self._started

if __name__ == "__main__":
    a = Stopwatch()
    time.sleep(4)
    print(a.get_elapsed())
