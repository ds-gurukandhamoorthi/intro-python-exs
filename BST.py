from TreeNode import TreeNode
class BinarySearchTree:
    def __init__(self):
        self._root = None

    def _get(self, node, key):
        if node is None:
            raise KeyError
        if key < node.key:
            return self._get(node.left, key)
        if key > node.key:
            return self._get(node.right, key)
        return node.val

    def __getitem__(self, key):
        return self._get(self._root, key)

    def _set(self, node, key, val):
        if node is None:
            return TreeNode(key, val)
        if key < node.key:
            node.left = self._set(node.left, key, val)
        elif key > node.key:
            node.right = self._set(node.right, key, val)
        else:
            node.val = val
        return node

    def __setitem__(self, key, val):
        self._root = self._set(self._root, key, val)

    def _contains(self, node, key):
        if node is None:
            return False
        if key < node.key:
            return self._contains(node.left, key)
        if key > node.key:
            return self._contains(node.right, key)
        return True

    def __contains__(self, key):
        return self._contains(self._root, key)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def _inorder_pair(self, node):
        if node:
            yield from self._inorder_pair(node.left)
            yield node.key, node.val
            yield from self._inorder_pair(node.right)

    def items(self):
        yield from self._inorder_pair(self._root)

    def __iter__(self):
        yield from self._inorder(self._root)

    def _min(self, node):
        if node:
            if node.left:
                return self._min(node.left)
            else:
                return node.key

    def min(self):
        return self._min(self._root)


    def _within_inclusive(self, node, minkey, maxkey):
        if node:
            if minkey <= node.key <= maxkey:
                yield node.key
            yield from self._within_inclusive(node.left, minkey, maxkey)
            yield from self._within_inclusive(node.right, minkey, maxkey)

    def within_inclusive(self, minkey, maxkey):
        yield from self._within_inclusive(self._root, minkey, maxkey)



            







if __name__ == "__main__":
    bst = BinarySearchTree()
    bst['name'] = 'guru'
    bst['age'] = 37
    print(bst['name'])
    print(bst['age'])
    print('age' in bst, 'AGE' in bst)
    # print(tuple(bst))
    print(tuple(bst))
    print(min(bst))
    print(bst.min())
    print(list(bst.within_inclusive('a','mame')))
    for k, v in bst.items():
        print(k, v)
    print (' %s' % list(bst.items()))

