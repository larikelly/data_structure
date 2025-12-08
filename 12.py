# Exercício 12:
# Implementar as classes LinkedStack, LinkedQueue, CircularQueue e LinkedDeque.

class Node:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = Node(e, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        return value

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.element

    def __str__(self):
        cur = self.head
        items = []
        while cur:
            items.append(str(cur.element))
            cur = cur.next
        return "LinkedStack(top→bottom): " + " -> ".join(items)

class LinkedQueue:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # rear
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        new = Node(e)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.element

    def __str__(self):
        cur = self.head
        items = []
        while cur:
            items.append(str(cur.element))
            cur = cur.next
        return "LinkedQueue(front→rear): " + " -> ".join(items)

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        new = Node(e)
        if self.is_empty():
            new.next = new
        else:
            new.next = self.tail.next
            self.tail.next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        old_head = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = old_head.next
        self.size -= 1
        return old_head.element

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.tail.next.element

    def rotate(self):
        if not self.is_empty():
            self.tail = self.tail.next

    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        items = []
        cur = self.tail.next
        for _ in range(self.size):
            items.append(str(cur.element))
            cur = cur.next
        return "CircularQueue: " + " -> ".join(items)

class LinkedDeque:
    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        self._add_between(e, self.header, self.header.next)

    def add_last(self, e):
        self._add_between(e, self.trailer.prev, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self.trailer.prev)

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.header.next.element

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.trailer.prev.element

    # Internal Helpers
    def _add_between(self, e, predecessor, successor):
        new = Node(e, successor, predecessor)
        predecessor.next = new
        successor.prev = new
        self.size += 1

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        return node.element

    def __str__(self):
        items = []
        cur = self.header.next
        while cur != self.trailer:
            items.append(str(cur.element))
            cur = cur.next
        return "LinkedDeque(front↔back): " + " <-> ".join(items)


def main():
    print("\n===== TESTE: LINKED STACK =====")
    S = LinkedStack()
    S.push(10)
    S.push(20)
    S.push(30)
    print(S)
    print("pop:", S.pop())
    print(S)

    print("\n===== TESTE: LINKED QUEUE =====")
    Q = LinkedQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(Q)
    print("dequeue:", Q.dequeue())
    print(Q)

    print("\n===== TESTE: CIRCULAR QUEUE =====")
    CQ = CircularQueue()
    CQ.enqueue(5)
    CQ.enqueue(6)
    CQ.enqueue(7)
    print(CQ)
    print("dequeue:", CQ.dequeue())
    print(CQ)
    CQ.rotate()
    print("rotate:", CQ)

    print("\n===== TESTE: LINKED DEQUE =====")
    D = LinkedDeque()
    D.add_first(9)
    D.add_last(8)
    D.add_first(7)
    print(D)
    print("delete_first:", D.delete_first())
    print(D)
    print("delete_last:", D.delete_last())
    print(D)

if __name__ == "__main__":
    main()
