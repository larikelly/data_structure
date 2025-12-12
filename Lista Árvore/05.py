# EXERCÍCIO 5.
# Verifique se uma árvore é uma ÁRVORE SOMA.

class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def soma_tree(node):
    if node is None:
        return 0, True

    if node.left is None and node.right is None:
        return node.element, True

    L, okL = soma_tree(node.left)
    R, okR = soma_tree(node.right)

    return (L + R + node.element), (okL and okR and node.element == L + R)

if __name__ == "__main__":
    T = Node(10, Node(4), Node(6))
    print("É soma tree?", soma_tree(T)[1])
