class Stack:
    def __init__(self):
        self._a = []

    def __bool__(self):
        return len(self) != 0

    def __len__(self):
        return len(self._a)

    def push(self, val):
        self._a += [val]

    def pop(self):
        if self:
            return self._a.pop()
    def __str__(self):
        return ' '.join(str(val) for val in reversed(self._a))
            
def main():
    s = Stack()
    print(len(s))
    s.push(3)
    s.push(4)
    # print(s.pop())
    # print(s.pop())
    if s:
        print(s)
if __name__ == "__main__":
    main()

