# EXERCÍCIO 1.
# Implemente a classe de árvores binárias LinkedBinaryTree usando
# uma estrutura encadeada conforme descrito na Seção 8.3.1.

class LinkedBinaryTree:
    class Node:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def add_root(self, e):
        self.root = self.Node(e)
        return self.root

    def add_left(self, node, e):
        node.left = self.Node(e)
        return node.left

    def add_right(self, node, e):
        node.right = self.Node(e)
        return node.right

if __name__ == "__main__":
    T = LinkedBinaryTree()
    r = T.add_root(10)
    L = T.add_left(r, 5)
    R = T.add_right(r, 20)
    print("Raiz:", T.root.element)
    print("Esquerda:", T.root.left.element)
    print("Direita:", T.root.right.element)
