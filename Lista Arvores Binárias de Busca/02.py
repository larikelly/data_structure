# EXERCÍCIO 2.
# Implemente a classe de árvores AVL (AVLTreeMap)
# descrita na Seção 11.3.2.

class AVLTree:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    def insert(self, key, value):
        def _insert(node, key, value):
            if node is None:
                return AVLTree.Node(key, value)

            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value
                return node

            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance_factor(node)

            if balance > 1 and key < node.left.key:
                return self.rotate_right(node)
            if balance < -1 and key > node.right.key:
                return self.rotate_left(node)
            if balance > 1 and key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = _insert(self.root, key, value)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node:
            self.print_tree(node.right, level + 1)
            print("   " * level, node.key)
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    T = AVLTree()
    for k in [30, 40, 24, 58, 48, 26, 11, 13]:
        T.insert(k, k)
    T.print_tree()
