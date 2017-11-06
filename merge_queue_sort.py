import sys
import random
from strutils import words
from Queue import Queue


def merge(queue1, queue2):
    res = Queue()
    while queue1 or queue2:
        if not queue2:
            while queue1:
                res.enqueue(queue1.dequeue())
            return res
        if not queue1:
            while queue2:
                res.enqueue(queue2.dequeue())
            return res
        v1, v2 = queue1.peek(), queue2.peek()
        if v1 <= v2:
            res.enqueue(queue1.dequeue())
        else:
            res.enqueue(queue2.dequeue())
    return res

def merge_sort(array):
    queue = Queue()
    for val in array:
        q = Queue()
        q.enqueue(val)
        queue.enqueue(q)
    while len(queue) > 1:
        q1 = queue.dequeue()
        q2 = queue.dequeue()
        queue.enqueue(merge(q1, q2))
    return tuple(queue.dequeue())






if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(4)
    b = Queue()
    b.enqueue(2)
    b.enqueue(5)
    b.enqueue(6)
    print(merge(a, b))
    a = [random.randrange(10) for i in range(100)]
    print(merge_sort(a))
    filename = sys.argv[1]
    with open(filename) as lines:
        wordslist = [word for line in lines for word in words(line)]
    print(merge_sort(wordslist))
