import sys


class Node:

    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.height = 0

    def replace_child(self, previous, new):
        """Replace the child with new one"""
        if self.left_child == previous:
            self.left_child = new
        elif self.right_child == previous:
            self.right_child = new
        if previous is not None:
            previous.parent = None
        if new is not None:
            new.parent = self

    def successor(self):
        """Finds the next largest node if present"""
        if self.right_child is not None:  # case 1: the node has a right child
            current = self.right_child
            while current.left_child is not None:  # find the smallest one in the node's right subtree
                current = current.left_child
            return current

        else:  # case 2: the node does not have a right child
            current = self
            while current.parent is not None:  # traverse up
                if current == current.parent.left_child:
                    return current.parent
                else:
                    current = current.parent

            return None  # the root is reached, so no successor exists

    def rotate_right(self):
        """Perform a right AVL rotation on the node"""
        left = self.left_child
        subtree = left.right_child
        parent = self.parent
        parent.replace_child(self, left)
        left.replace_child(subtree, self)
        self.replace_child(left, subtree)

    def rotate_left(self):
        """Perform a left AVL rotation on the node"""
        right = self.right_child
        subtree = right.left_child
        parent = self.parent
        parent.replace_child(self, right)
        right.replace_child(subtree, self)
        self.replace_child(right, subtree)

    def double_avl_left(self):
        """Perform AVL rotation on a left kink"""
        left = self.left_child
        left.rotate_left()
        self.rotate_right()

    def double_avl_right(self):
        """Perform AVL rotation on a right kink"""
        right = self.right_child
        right.rotate_right()
        self.rotate_left()


class AVLTree:

    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        """Returns the number of nodes in the tree"""
        return self._size

    def clear(self):
        """Clears the tree"""
        # TODO: clean memory
        self.root = None
        self._size = 0

    def empty(self):
        """Check if the tree is empty"""
        return True if self._size == 0 else False

    def find(self, value):
        """Returns True if value exists in the tree, otherwise returns False"""
        current = self.root  # start at the root
        while value != current.value:

            if value < current.value:  # traverse left
                current = current.left_child

            elif value > current.value:  # traverse right
                current = current.right_child

            if current is None:  # failure
                return False

        return True

    def insert(self, value):
        """Inserts value in the tree and returns True on success or False on failure"""
        if self.empty():  # empty tree, so value becomes the root
            self.root = Node(value)
            self._size += 1
            return True

        current = self.root  # start at the root
        while current.value != value:

            if value < current.value:

                if current.left_child is None:  # if no left child exists, insert value as left child
                    current.left_child = Node(value)
                    current.left_child.parent = current
                    self._size += 1
                    return True

                else:  # if a left child does exist, traverse left
                    current = current.left_child

            elif value > current.value:

                if current.right_child is None:  # if no right child exists, insert value as right child
                    current.right_child = Node(value)
                    current.right_child.parent = current
                    self._size += 1
                    return True

                else:  # if a right child does exist, traverse right
                    current = current.right_child

        return False  # failure to insert

    def remove(self, value):
        """Removes value if it exists in the tree (returns True), or returns False otherwise"""
        current = self.root  # start at the root
        while current.value != value:

            if value < current.value:  # traverse left
                current = current.left_child
            elif value > current.value:  # traverse right
                current = current.right_child

            if current is None:  # if no such value, failure
                return False

        # value is present in tree
        if current.left_child is None and current.right_child is None:  # case 1: no children
            current.parent.replace_child(current, None)
            del current

        elif current.left_child is not None and current.right_child is None:  # case 2: only left child
            current.parent.replace_child(current, current.left_child)
            del current

        elif current.left_child is None and current.right_child is not None:  # case 3: only right child
            current.parent.replace_child(current, current.right_child)
            del current

        else:  # case 4: two children
            successor = current.successor()
            # successor is the right child of current or the leftmost node in current's right subtree
            successor.parent.replace_child(successor, successor.right_child)
            current.value = successor.value
            del successor

        self._size -= 1
        return True

    def in_order(self):
        """In-order traversal over the values of the tree"""
        current = self.root  # start at the root

        if current is None:
            return

        while current.left_child is not None:
            current = current.left_child

        while current is not None:
            yield current.value
            current = current.successor()


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        op, *args = sys.stdin.readline().strip().split(" ")


def test_bst_properties():
    tree = AVLTree()
    for x in ([9, 3, 11, 10, 12, 6, 4, 8, 7]):
        tree.insert(x)
    assert list(tree.in_order()) == [3, 4, 6, 7, 8, 9, 10, 11, 12]
    assert tree.find(10)
    assert tree.size() == 9
    assert not tree.remove(16)
    assert tree.remove(10)
    assert tree.size() == 8
    assert list(tree.in_order()) == [3, 4, 6, 7, 8, 9, 11, 12]
    assert not tree.find(10)
    assert tree.size() == 8
    tree.clear()
    assert tree.size() == 0
    assert list(tree.in_order()) == []
    for x in ([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        tree.insert(x)
    assert tree.size() == 9
    assert not tree.find(25)
    assert tree.find(9)
    assert tree.remove(5)
    assert tree.remove(3)
    assert tree.remove(7)
    assert list(tree.in_order()) == [1, 2, 4, 6, 8, 9]
    assert tree.size() == 6
    assert not tree.empty()
    tree.clear()
