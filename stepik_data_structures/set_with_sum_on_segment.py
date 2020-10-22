import sys


class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class AVLTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, value):
        current = self.root
        while value != current.value:

            if value < current.value:
                current = current.left_child

            elif value > current.value:
                current = current.right_child

            if current is None:
                return False

        return True

    def insert(self, value):
        if not self.find(value):
            self.root = Node(value)
            self.size += 1
            return True

        current = self.root
        while current.value != value:

            if value < current.value:
                if current.left_child is None:
                    current.left_child = Node(value)
                    current.left_child.parent = current
                    self.size += 1
                    return True
                else:
                    current = current.left_child

            elif value > current.value:
                if current.right_child is None:
                    current.right_child = Node(value)
                    current.right_child.parent = current
                    self.size += 1
                    return True
                else:
                    current = current.right_child

        return False

    def AVLRight(self, node):
        left = node.left_child
        right = node.right_child
        parent = node.parent
        if parent is not None and node is parent.right_child:
            pass

    def remove(self, value):
        current = self.find(value)
        if current.left_child is None and current.right_child is None:
            pass
        elif current.left_child is None or current.right_child is None:
            pass
        else:
            pass

    def successor(self, node):
        if node.right_child is not None:
            current = node.right_child
            while current.left_child is not None:
                current = current.left_child
            return current
        else:
            current = node
            while current.parent is not None:
                if current == current.parent.left_child:
                    return current.parent
                else:
                    current = current.parent
            return None

    def size(self):
        return self.size

    def clear(self):
        self.root = None
        self.size = 0

    def empty(self):
        return True if self.size == 0 else False


def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        op, *args = sys.stdin.readline().strip().split(" ")

