# EXERCÍCIO 2:
# Execute a seguinte série de operações de pilha, assumindo
# uma pilha inicialmente vazia:
# push(5), push(3), pop(), push(2), push(8), pop(), pop(),
# push(9), push(1), pop(), push(7), push(6), pop(), pop(),
# push(4), pop(), pop().

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

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]

    def __str__(self):
        return str(self._data)


def exercise_2_execution():
    S = ArrayStack()
    operations = [
        ('push', 5), ('push', 3), ('pop', None), ('push', 2), ('push', 8),
        ('pop', None), ('pop', None), ('push', 9), ('push', 1), ('pop', None),
        ('push', 7), ('push', 6), ('pop', None), ('pop', None), ('push', 4),
        ('pop', None), ('pop', None)
    ]

    print("\n--- Exercício 2: Execução de Operações de Pilha ---\n")

    for op, val in operations:
        if op == 'push':
            S.push(val)
            print(f"push({val})  -> Pilha: {S}")
        elif op == 'pop':
            removed = S.pop()
            print(f"pop() = {removed} -> Pilha: {S}")


if __name__ == "__main__":
    exercise_2_execution()
