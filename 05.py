# EXERCÍCIO 5:
# Implemente uma função que inverte uma lista de elementos
# colocando-os em uma pilha em uma ordem e escrevendo-os de
# volta na lista na ordem inversa.

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()

    def __str__(self):
        return str(self._data)

def reverse_list_with_stack(lst):
    S = ArrayStack()
    for item in lst:
        S.push(item)
    for i in range(len(lst)):
        lst[i] = S.pop()
def main():
    lista = [1, 2, 3, 4, 5]
    print("Lista antes:", lista)

    reverse_list_with_stack(lista)

    print("Lista depois:", lista)


if __name__ == "__main__":
    main()
