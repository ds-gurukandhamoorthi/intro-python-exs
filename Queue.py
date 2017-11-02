from Node import Node


class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

    def __bool__(self):
        return self._first is not None

    def enqueue(self, val):
        node = Node(val, None)
        if self:
            prev_last = self._last
            self._last = node
            prev_last.ref_next = self._last
        else:
            self._first = node
            self._last = node
        self._len += 1

    def dequeue(self):
        if self:
            val = self._first.item
            self._first = self._first.ref_next
            self._len -= 1
            if self._len == 0:
                self._last = None
            return val
        else:
            raise Exception('Trying to dequeue from an empty Queue')

    def peek(self):
        if self:
            return self._first.item
        else:
            raise Exception('Trying to peek into an empty Queue')

    def __len__(self):
        return self._len

    def __iter__(self):
        curr = self._first
        while curr:
            val, curr = curr.item, curr.ref_next
            yield val

    def __str__(self):
        return ' '.join(str(val) for val in tuple(self))


def main():
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(tuple(q))
    if q:
        print(q)


if __name__ == "__main__":
    main()
