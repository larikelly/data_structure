# EXERCÍCIO 8:
# Escreva um programa para verificar se em uma string contendo
# uma expressão aritmética, os parênteses de abertura e fechamento
# estão bem formados ou não.

class ArrayStack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()


def parentheses_well_formed(expr):
    S = ArrayStack()

    for char in expr:
        if char == '(':
            S.push(char)
        elif char == ')':
            if S.is_empty():
                return False  
            S.pop()

    return S.is_empty()


def main():
    expr = input("Digite a expressão: ")

    if parentheses_well_formed(expr):
        print("Os parênteses estão bem formados.")
    else:
        print("Os parênteses NÃO estão bem formados.")


if __name__ == "__main__":
    main()
