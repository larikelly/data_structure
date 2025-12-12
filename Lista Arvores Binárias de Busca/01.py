# EXERCÍCIO 1.
# Implemente a classe de árvores binárias de busca TreeMap
# descrita na Seção 11.1.4.

class BSTMap:
    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        def _insert(node, key, value):
            if node is None:
                return self.Node(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value  # update
            return node
        self.root = _insert(self.root, key, value)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("   " * level, node.key)
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    t = BSTMap()
    for k in [30, 40, 24, 58, 48, 26, 11, 13]:
        t.insert(k, k)
    t.print_tree()
