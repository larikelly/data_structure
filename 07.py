# EXERCÍCIO 7:
# Execute a seguinte série de operações de deque, assumindo uma
# deque inicialmente vazia:
# add first(4), add last(8), add last(9), add first(5), back(),
# delete first(), delete last(), add last(7), first(), last(),
# add last(6), delete first(), delete first().

class ArrayDeque:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data[-1]

    def __str__(self):
        return str(self._data)

def exercise_deque_execution():
    D = ArrayDeque()

    operations = [
        ("add_first", 4),
        ("add_last", 8),
        ("add_last", 9),
        ("add_first", 5),
        ("back", None),
        ("delete_first", None),
        ("delete_last", None),
        ("add_last", 7),
        ("first", None),
        ("last", None),
        ("add_last", 6),
        ("delete_first", None),
        ("delete_first", None),
    ]

    print("\n--- Exercício: Execução de Operações de Deque ---\n")

    for op, val in operations:
        if op == "add_first":
            D.add_first(val)
            print(f"add_first({val}) -> {D}")

        elif op == "add_last":
            D.add_last(val)
            print(f"add_last({val}) -> {D}")

        elif op == "delete_first":
            removed = D.delete_first()
            print(f"delete_first() = {removed} -> {D}")

        elif op == "delete_last":
            removed = D.delete_last()
            print(f"delete_last() = {removed} -> {D}")

        elif op == "first":
            print(f"first() = {D.first()} -> {D}")

        elif op == "last":
            print(f"last() = {D.last()} -> {D}")

        elif op == "back":
            print(f"back() = {D.last()} -> {D}")


if __name__ == "__main__":
    exercise_deque_execution()
