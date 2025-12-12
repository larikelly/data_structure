# EXERCÍCIO 2.
# Implemente a classe ArrayBinaryTree baseada em array conforme
# descrito na Seção 8.3.2.

class ArrayBinaryTree:
    def __init__(self):
        self.data = [None] * 100 
        self.size = 0

    def add_root(self, e):
        self.data[1] = e
        self.size = 1
        return 1

    def add_left(self, index, e):
        self.data[index * 2] = e
        self.size += 1
        return index * 2

    def add_right(self, index, e):
        self.data[index * 2 + 1] = e
        self.size += 1
        return index * 2 + 1


if __name__ == "__main__":
    T = ArrayBinaryTree()
    r = T.add_root(50)
    L = T.add_left(r, 30)
    R = T.add_right(r, 70)
    print(T.data[:10])
