# EXERCÍCIO 7.
# Encontrar e imprimir os ancestrais de um nó específico.

class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def encontrar_ancestrais(node, alvo, caminho=[]):
    if node is None:
        return False

    if node.element == alvo:
        print("Ancestrais:", caminho)
        return True

    caminho.append(node.element)

    if encontrar_ancestrais(node.left, alvo, caminho): return True
    if encontrar_ancestrais(node.right, alvo, caminho): return True

    caminho.pop()
    return False

if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    encontrar_ancestrais(root, 5)
