# EXERCÍCIO 8.
# Substituir cada nó pela soma de todos os valores de suas
# subárvores esquerda e direita.

class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def substituir_por_soma(node):
    if node is None:
        return 0

    L = substituir_por_soma(node.left)
    R = substituir_por_soma(node.right)

    old = node.element
    node.element = L + R
    return old + node.element

if __name__ == "__main__":
    root = Node(10, Node(4), Node(6))
    substituir_por_soma(root)
    print("Raiz agora vale:", root.element)
