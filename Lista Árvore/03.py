# EXERCÍCIO 3.
# Implementar Preorder, Inorder e Postorder para a LinkedBinaryTree.

class LinkedBinaryTree:
    class Node:
        def __init__(self, e, left=None, right=None):
            self.element = e
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self.root = root


def preorder(node):
    if node:
        print(node.element, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.element, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.element, end=" ")

if __name__ == "__main__":
    n4 = LinkedBinaryTree.Node(4)
    n5 = LinkedBinaryTree.Node(5)
    n2 = LinkedBinaryTree.Node(2, n4, n5)
    n3 = LinkedBinaryTree.Node(3)
    n1 = LinkedBinaryTree.Node(1, n2, n3)

    print("Preorder:")
    preorder(n1)
    print("\nInorder:")
    inorder(n1)
    print("\nPostorder:")
    postorder(n1)
