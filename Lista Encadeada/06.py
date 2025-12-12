# EXERCÍCIO 6:
# Execute a seguinte série de operações de fila, assumindo uma
# fila inicialmente vazia:
# enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8),
# dequeue(), dequeue(), enqueue(9), enqueue(1), dequeue(),
# enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4),
# dequeue(), dequeue().

class ArrayQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[0]

    def __str__(self):
        return str(self._data)
def exercise_queue_execution():
    Q = ArrayQueue()
    operations = [
        ('enqueue', 5), ('enqueue', 3), ('dequeue', None),
        ('enqueue', 2), ('enqueue', 8), ('dequeue', None),
        ('dequeue', None), ('enqueue', 9), ('enqueue', 1),
        ('dequeue', None), ('enqueue', 7), ('enqueue', 6),
        ('dequeue', None), ('dequeue', None), ('enqueue', 4),
        ('dequeue', None), ('dequeue', None)
    ]

    print("\n--- Exercício: Execução de Operações de Fila ---\n")

    for op, val in operations:
        if op == 'enqueue':
            Q.enqueue(val)
            print(f"enqueue({val})  -> Fila: {Q}")
        elif op == 'dequeue':
            removed = Q.dequeue()
            print(f"dequeue() = {removed} -> Fila: {Q}")


if __name__ == "__main__":
    exercise_queue_execution()
