# EXERCÍCIO 3.
# Implemente a classe de árvores rubro-negras RedBlackTreeMap
# descrita na Seção 11.6.2.

RED = True
BLACK = False

class RBTree:
    class Node:
        def __init__(self, key, value, color=RED):
            self.key = key
            self.value = value
            self.color = color
            self.left = None
            self.right = None

    def is_red(self, node):
        return node is not None and node.color == RED

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def flip_colors(self, h):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        def _insert(h, key, value):
            if h is None:
                return RBTree.Node(key, value)

            if key < h.key:
                h.left = _insert(h.left, key, value)
            elif key > h.key:
                h.right = _insert(h.right, key, value)
            else:
                h.value = value

            if self.is_red(h.right) and not self.is_red(h.left):
                h = self.rotate_left(h)
            if self.is_red(h.left) and self.is_red(h.left.left):
                h = self.rotate_right(h)
            if self.is_red(h.left) and self.is_red(h.right):
                self.flip_colors(h)

            return h

        self.root = _insert(self.root, key, value)
        self.root.color = BLACK  

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node:
            self.print_tree(node.right, level + 1)
            color = "R" if node.color == RED else "B"
            print("   " * level, f"{node.key}({color})")
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    T = RBTree()
    for k in [5,16,22,45,2,10,18,30,50,12,1]:
        T.insert(k, k)
    T.print_tree()
