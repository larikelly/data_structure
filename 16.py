# EXERCÍCIO 16:
# Implemente uma função que conta o número de nós
# em uma lista circularmente encadeada.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def contar_nos_lista_circular(head):
    """Conta nós em uma lista circular encadeada."""
    if head is None:
        return 0

    count = 1
    atual = head.next

    while atual is not None and atual != head:
        count += 1
        atual = atual.next

    return count

if __name__ == "__main__":
    print("EXERCÍCIO 16 - Contagem em lista circular\n")

    a = Node(10)
    b = Node(20)
    c = Node(30)

    a.next = b
    b.next = c
    c.next = a 

    print("Número de nós (lista circular):", contar_nos_lista_circular(a))
