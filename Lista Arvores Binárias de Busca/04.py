# EXERCÍCIO 4.
# Insira em uma BST vazia as chaves:
# 30,40,24,58,48,26,11,13 (nesta ordem)
# Imprima a árvore após cada inserção.

from time import sleep

class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return BST.Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node:
            self.print_tree(node.right, level+1)
            print("   "*level, node.key)
            self.print_tree(node.left, level+1)

if __name__ == "__main__":
    T = BST()
    keys = [30,40,24,58,48,26,11,13]
    for k in keys:
        T.insert(k)
        print(f"\nApós inserir {k}:")
        T.print_tree()
