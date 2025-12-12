# EXERCÍCIO 4.
# Verificar se duas árvores binárias são idênticas.

class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def arvores_identicas(a, b):
    if a is None and b is None:
        return True
    if a and b:
        return (a.element == b.element and
                arvores_identicas(a.left, b.left) and
                arvores_identicas(a.right, b.right))
    return False


if __name__ == "__main__":
    A = Node(1, Node(2), Node(3))
    B = Node(1, Node(2), Node(3))
    C = Node(1, Node(4), Node(5))
    print("A e B idênticas?", arvores_identicas(A, B))
    print("A e C idênticas?", arvores_identicas(A, C))
