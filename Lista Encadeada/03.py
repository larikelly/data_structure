# EXERCÍCIO 3:
# Implemente uma função com assinatura transfer(S, T) que
# transfira todos os elementos da pilha S para a pilha T, de
# modo que o elemento que começa no topo de S seja o primeiro
# a ser inserido em T, e o elemento na parte inferior de S
# termine no topo de T.

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


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


def main():
    S = ArrayStack()
    T = ArrayStack()

    S.push(1)
    S.push(2)
    S.push(3)

    print("Antes da transferência:")
    print("S:", S)
    print("T:", T)

    transfer(S, T)

    print("\nDepois da transferência:")
    print("S:", S)
    print("T:", T)


if __name__ == "__main__":
    main()
