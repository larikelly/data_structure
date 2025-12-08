# Exercício 15:
# Descreva um algoritmo recursivo que conta o número de nós
# em uma lista encadeada simples.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def contar_nos_recursivo(head):
    """Conta nós recursivamente em uma lista encadeada simples."""
    if head is None:
        return 0
    return 1 + contar_nos_recursivo(head.next)
if __name__ == "__main__":
    print("EXERCÍCIO 15 - Contagem recursiva de nós\n")

    lista = Node(1, Node(2, Node(3, Node(4))))

    # Impressão da lista
    atual = lista
    while atual:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")

    print("Número de nós:", contar_nos_recursivo(lista))
