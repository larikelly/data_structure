# Exercício 11:
# Usar uma pilha e uma fila para testar se uma string é um palíndromo.

class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0


def is_palindrome(s):
    stack = Stack()
    queue = Queue()

    s = ''.join(c.lower() for c in s if c.isalnum())

    for ch in s:
        stack.push(ch)
        queue.enqueue(ch)

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False

    return True

if __name__ == "__main__":
    frases = ["arara", "radar", "Ame a ema", "banana", "Socorram-me subi no ônibus em Marrocos"]

    for f in frases:
        print(f"'{f}' → Palíndromo? {is_palindrome(f)}")
