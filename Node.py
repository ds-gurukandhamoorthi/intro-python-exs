class Node:
    def __init__(self, item, ref_next):
        self.item = item
        self.ref_next = ref_next

    def __bool__(self):
        return self is not None
