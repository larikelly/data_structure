# EXERCÍCIO 19:
# Escreva um programa para excluir elementos duplicados
# em uma lista duplamente encadeada.

class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new = DNode(value)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def remover_duplicados(self):
        seen = set()
        atual = self.head

        while atual:
            if atual.value in seen:
                # remover nó duplicado
                if atual.prev:
                    atual.prev.next = atual.next
                if atual.next:
                    atual.next.prev = atual.prev
                if atual == self.tail:
                    self.tail = atual.prev
            else:
                seen.add(atual.value)
            atual = atual.next

    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.value, end=" <-> ")
            atual = atual.next
        print("None")


if __name__ == "__main__":
    print("EXERCÍCIO 19 - Remover duplicados de lista duplamente encadeada\n")

    lista = DoublyLinkedList()
    for x in [4, 2, 7, 2, 4, 9, 7]:
        lista.append(x)

    print("Lista original:")
    lista.imprimir()

    lista.remover_duplicados()

    print("\nLista sem duplicados:")
    lista.imprimir()
