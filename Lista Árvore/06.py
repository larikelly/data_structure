 # EXERCÍCIO 6.
# Imprimir todos os caminhos da raiz até cada folha.

class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def imprimir_caminhos(node, caminho=[]):
    if node is None:
        return

    caminho.append(node.element)

    if node.left is None and node.right is None:
        print(" -> ".join(map(str, caminho)))

    imprimir_caminhos(node.left, caminho)
    imprimir_caminhos(node.right, caminho)

    caminho.pop()

if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    imprimir_caminhos(root)
