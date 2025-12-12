# EXERCÍCIO 20:
# Modifique a classe DoublyLinkedBase para incluir um método reverse
# que inverte a ordem da lista sem criar ou destruir nenhum nó.

class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedBase:
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

    def reverse(self):
        """Inverte a lista sem criar nem destruir nós."""
        atual = self.head

        self.tail = self.head  

        prev = None
        while atual:
            atual.prev, atual.next = atual.next, atual.prev
            prev = atual
            atual = atual.prev  

        self.head = prev

    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.value, end=" <-> ")
            atual = atual.next
        print("None")


if __name__ == "__main__":
    print("EXERCÍCIO 20 - Inverter lista duplamente encadeada\n")

    lista = DoublyLinkedBase()
    for x in [10, 20, 30, 40, 50]:
        lista.append(x)

    print("Original:")
    lista.imprimir()

    lista.reverse()

    print("\nReversa:")
    lista.imprimir()
