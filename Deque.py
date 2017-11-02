from Node import Node


class LinkedStack:
    def __init__(self):
        self._first = None
        self._len = 0

    def __bool__(self):
        return self._first is not None

    def push(self, val):
        self._first = Node(val, self._first)
        self._len += 1

    def pop(self):
        if self:
            val = self._first.item
            self._first = self._first.ref_next
            self._len -= 1
            return val
        else:
            raise Exception('Trying to pop an empty Stack')

    def peek(self):
        if self:
            return self._first.item
        else:
            raise Exception('Trying to peek into an empty Stack')

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
    s = LinkedStack()
    s.push(3)
    s.push(4)
    print(5 in s, 3 in s)
    print(len(s))
    # print(s.pop())
    print(tuple(s))
    if s:
        print(s)


if __name__ == "__main__":
    main()
