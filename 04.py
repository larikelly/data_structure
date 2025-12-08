# EXERCÍCIO 4:
# Forneça um método recursivo para remover todos os elementos
# de uma pilha.

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


def clear_recursive(S):
    if S.is_empty():
        return
    S.pop()
    clear_recursive(S)


def main():
    S = ArrayStack()
    S.push(10)
    S.push(20)
    S.push(30)

    print("Antes:", S)
    clear_recursive(S)
    print("Depois:", S)


if __name__ == "__main__":
    main()
