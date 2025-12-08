# Exercício 13:
# Fornecer um algoritmo para encontrar o penúltimo nó de uma lista encadeada simples,
# onde o último nó aponta para None.

class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

def find_penultimate(head):
    """
    Retorna o penúltimo nó de uma lista encadeada simples.
    Se a lista tiver 0 ou 1 elemento, retorna None.
    """
    if head is None or head.next is None:
        return None  

    cur = head

    while cur.next.next is not None:
        cur = cur.next

    return cur

def create_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    cur = head

    for val in values[1:]:
        cur.next = Node(val)
        cur = cur.next

    return head

def print_list(head):
    items = []
    cur = head
    while cur:
        items.append(str(cur.element))
        cur = cur.next
    print("Lista: " + " -> ".join(items) + " -> None")


def main():
    print("\n=== TESTE 1: Lista com vários elementos ===")
    head = create_linked_list([10, 20, 30, 40])
    print_list(head)
    pen = find_penultimate(head)
    print("Penúltimo nó:", pen.element if pen else "None")

    print("\n=== TESTE 2: Lista com 2 elementos ===")
    head = create_linked_list([99, 100])
    print_list(head)
    pen = find_penultimate(head)
    print("Penúltimo nó:", pen.element if pen else "None")

    print("\n=== TESTE 3: Lista com 1 elemento ===")
    head = create_linked_list([42])
    print_list(head)
    pen = find_penultimate(head)
    print("Penúltimo nó:", pen.element if pen else "None")

    print("\n=== TESTE 4: Lista vazia ===")
    head = create_linked_list([])
    print_list(head)
    pen = find_penultimate(head)
    print("Penúltimo nó:", pen.element if pen else "None")

if __name__ == "__main__":
    main()
