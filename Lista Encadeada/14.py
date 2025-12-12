# Exercicio 14:
# Descreva um bom algoritmo para concatenar duas listas encadeadas
# simples L e M, dadas apenas referências ao primeiro nó de cada lista,
# em uma única lista L que contenha todos os nós de L seguidos por todos
# os nós de M.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def concatenar_listas(L, M):
    """
    Concatena duas listas encadeadas simples L e M.
    Retorna a lista L contendo seus nós seguidos dos nós de M.
    """
    if L is None:
        return M
    if M is None:
        return L
    atual = L
    while atual.next is not None:
        atual = atual.next
    atual.next = M

    return L


def imprimir_lista(head):
    """Função auxiliar para imprimir a lista ligada."""
    atual = head
    while atual is not None:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")

if __name__ == "__main__":

    L = Node(1, Node(2, Node(3)))
    M = Node(4, Node(5, Node(6)))

    print("Lista L:")
    imprimir_lista(L)

    print("Lista M:")
    imprimir_lista(M)

    L = concatenar_listas(L, M)

    print("Lista concatenada L + M:")
    imprimir_lista(L)
