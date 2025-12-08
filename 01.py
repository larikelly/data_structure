# EXERCÍCIO 1:
# Implemente as classes ArrayStack, ArrayQueue e ArrayDeque.

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

def main():
    print("\n--- Testando ArrayStack ---")
    S = ArrayStack()
    S.push(1)
    S.push(2)
    S.push(3)
    print("Stack:", S)
    S.pop()
    print("Após pop:", S)

    print("\n--- Testando ArrayQueue ---")
    Q = ArrayQueue()
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)
    print("Queue:", Q)
    Q.dequeue()
    print("Após dequeue:", Q)

    print("\n--- Testando ArrayDeque ---")
    D = ArrayDeque()
    D.add_first(5)
    D.add_last(10)
    D.add_last(15)
    print("Deque:", D)
    D.delete_first()
    print("Após delete_first:", D)
    D.delete_last()
    print("Após delete_last:", D)

if __name__ == "__main__":
    main()
