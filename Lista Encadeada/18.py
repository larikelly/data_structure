# EXERCÍCIO 18:
# Uma lista encadeada contém números positivos e números negativos.
# Usando essa lista, escreva um programa que crie duas novas listas:
# - uma contendo apenas números positivos
# - outra contendo apenas números negativos

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def separar_positivos_negativos(head):
    positivos_head = positivos_tail = None
    negativos_head = negativos_tail = None

    atual = head
    while atual:
        novo = Node(atual.value)

        if atual.value >= 0:
            if positivos_head is None:
                positivos_head = positivos_tail = novo
            else:
                positivos_tail.next = novo
                positivos_tail = novo
        else:
            if negativos_head is None:
                negativos_head = negativos_tail = novo
            else:
                negativos_tail.next = novo
                negativos_tail = novo

        atual = atual.next

    return positivos_head, negativos_head


def imprimir_lista(head):
    atual = head
    while atual:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")

if __name__ == "__main__":
    print("EXERCÍCIO 18 - Separar positivos e negativos\n")

    lista = Node(3, Node(-1, Node(7, Node(-5, Node(2, Node(-9))))))

    print("Lista original:")
    imprimir_lista(lista)

    pos, neg = separar_positivos_negativos(lista)

    print("\nPositivos:")
    imprimir_lista(pos)

    print("Negativos:")
    imprimir_lista(neg)
