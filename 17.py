# EXERCÍCIO 17:
# Descreva um algoritmo recursivo rápido para reverter
# uma lista encadeada simples.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverter_lista_recursivo(head):
    """
    Reverte uma lista encadeada simples usando recursão.
    Retorna o novo head.
    """
    if head is None or head.next is None:
        return head

    novo_head = reverter_lista_recursivo(head.next)

    head.next.next = head
    head.next = None

    return novo_head


def imprimir_lista(head):
    atual = head
    while atual:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")

if __name__ == "__main__":
    print("EXERCÍCIO 17 - Reversão recursiva\n")

    lista = Node(7, Node(8, Node(9, Node(10))))

    print("Antes:")
    imprimir_lista(lista)

    lista_invertida = reverter_lista_recursivo(lista)

    print("Depois:")
    imprimir_lista(lista_invertida)
