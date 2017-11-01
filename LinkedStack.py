from Node import Node


class LinkedStack:
    def __init__(self):
        self._first = None

    def __bool__(self):
        return self._first is not None

    def push(self, val):
        self._first = Node(val, self._first)

    def pop(self):
        if self:
            val = self._first.item
            self._first = self._first.ref_next
            return val

    def __iter__(self):
        curr = self._first
        while curr:
            val, curr = curr.item, curr.ref_next
            yield val

    def __str__(self):
        return ' '.join(str(val) for val in tuple(self))


def main():
    s = LinkedStack()
    # print(len(s))
    s.push(3)
    s.push(4)
    # print(s.pop())
    # print(s.pop())
    print(tuple(s))
    if s:
        print(s)


if __name__ == "__main__":
    main()
