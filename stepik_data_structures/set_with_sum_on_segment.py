import sys
from typing import Union


class Node:
    """Node class for binary search trees. Implements many useful methods."""

    def __init__(self, key):
        self.key: int = key
        self.sum: int = self.key  # if node is root, this is sum of elements of tree
        self.height: int = 1  # if node is root, this is height of tree
        self.size: int = 1  # if node is root, this is size of tree
        self.balance_factor: int = 0
        self.parent: Union[Node, None] = None
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None

    def __repr__(self):
        return f"Node {self.key}: {self.left_key} {self.right_key}; "

    @property
    def left_key(self):
        return self.left.key if self.left is not None else None

    @property
    def right_key(self):
        return self.right.key if self.right is not None else None

    # @property
    # def __left_height(self):
    #     """Get height of left subtree."""
    #     return self.left.height if self.left is not None else 0
    #
    # @property
    # def __right_height(self):
    #     """Get height of right subtree."""
    #     return self.right.height if self.right is not None else 0

    def __update_height(self):
        """Update height value of the node."""
        # self.height = max(self.__left_height, self.__right_height) + 1
        self.height = 1 + max(
            self.left.height if self.left is not None else 0,
            self.right.height if self.right is not None else 0
        )

    @property
    def __balance_factor(self):
        """Computes balance factor of the node."""
        print("Computing balance factor")
        return self.__right_height - self.__left_height

    # @property
    # def __left_sum(self):
    #     """Get sum of left subtree."""
    #     return self.left.sum if self.left is not None else 0
    #
    # @property
    # def __right_sum(self):
    #     """Get sum of right subtree."""
    #     return self.right.sum if self.right is not None else 0

    def __update_sum(self):
        """Update sum value of the node."""
        # self.sum = self.__left_sum + self.__right_sum + self.key
        self.sum = self.key + \
            self.left.sum if self.left is not None else 0 + \
            self.right.sum if self.right is not None else 0

    # @property
    # def __left_size(self):
    #     """Get size of left subtree."""
    #     return self.left.size if self.left is not None else 0
    #
    # @property
    # def __right_size(self):
    #     """Get size of right subtree."""
    #     return self.right.size if self.right is not None else 0

    def __update_size(self):
        """Update size of tree """
        self.size = self.__left_size + self.__right_size + 1

    def __update(self):
        self.__update_height()
        self.__update_size()
        self.__update_sum()

    def add_left(self, key):
        """Adds left child. Raises an exception when such child exists."""
        if self.left is None:
            if key >= self.key:
                raise ValueError("Key isn't less than parent's key")
            self.left = Node(key=key)
            self.left.parent = self
        else:
            raise ValueError("Left child exists")
        self.__update()

    def add_right(self, key):
        """Adds right child. Raises an exception when such child exists."""
        if self.right is None:
            if key <= self.key:
                raise ValueError("Key isn't bigger than parent's key")
            self.right = Node(key=key)
            self.right.parent = self
        else:
            raise ValueError("Right child exists")
        self.__update()

    def balance(self):

        if self.balance_factor == 2:  # right subtree is higher

            middle = self.right
            if middle.balance_factor < 0:  # left subtree of middle node is higher
                middle._rotate_right()
            return self._rotate_left()

        elif self.balance_factor == -2:  # left subtree is higher

            middle = self.left
            if middle.balance_factor > 0:  # right subtree of middle node is higher
                middle._rotate_left()
            return self._rotate_right()

        return self  # no rotations

    def _rotate_right(self):
        """Perform a right AVL rotation on the node. Returns new root of the whole subtree."""
        lower = self.left
        # add right subtree of lower to upper (self) as left child and update links
        self.left = lower.right
        self.left.parent = self
        self.__update()
        # update lower and upper links
        parent = self.parent
        lower.right = self
        self.parent = lower
        lower.__update()
        # update parent links
        lower.parent = parent
        if parent is not None and parent.left == self:
            parent.left = lower
        elif parent is not None and parent.right == self:
            parent.right = lower
        return lower

    def _rotate_left(self):
        """Perform a left AVL rotation on the node. Returns new root of the whole subtree."""
        lower = self.right
        # add left subtree of lower to upper (self) as right child and update links
        self.right = lower.left
        self.right.parent = self
        self.__update()
        # update lower and upper links
        parent = self.parent
        lower.left = self
        self.parent = lower
        lower.__update()
        # update parent links
        lower.parent = parent
        if parent is not None and parent.left == self:
            parent.left = lower
        elif parent is not None and parent.right == self:
            parent.right = lower
        return lower

    def successor(self):
        """Finds the next largest node."""
        if self.right is not None:  # case 1: the node has a right child
            current = self.right
            while current.left is not None:  # find the smallest one in the node's right subtree
                current = current.left
            return current

        else:  # case 2: the node does not have a right child
            current = self
            while current.parent is not None:  # traverse up
                if current == current.parent.left:
                    return current.parent
                else:
                    current = current.parent

            return None  # the root is reached, so no successor exists


class AVLTree:

    def __init__(self, root):
        self.root = root

    def empty(self):
        """Check if the tree is empty."""
        return True if self.root is None else False

    @property
    def size(self):
        """Returns the number of nodes in the tree."""
        return self.root.size if not self.empty() else 0

    @property
    def height(self):
        """Returns the height of the tree."""
        return self.root.height if not self.empty() else 0

    def clear(self):
        """Clears the tree."""
        stack = [self.root]

        while stack:  # removing all links in loop
            node = stack.pop()
            if node is None:
                continue
            node.parent = None
            if node.left is not None:
                stack.append(node.left)
                node.left = None
            if node.right is not None:
                stack.append(node.right)
                node.right = None

        self.root = None

    def _balance_tree(self, current: Node):

        while current != self.root:
            current = current.balance()  # balance node, may return other one
            current = current.parent  # go up
        self.root = current.balance()

    def _find(self, value):
        """Returns element with such value if it is in tree, otherwise returns None."""
        current = self.root  # start at the root
        while value != current.key:

            if value < current.key:
                current = current.left  # traverse left

            elif value > current.key:
                current = current.right  # traverse right

            if current is None:  # failure
                break

        return current

    def find(self, value):
        """Returns True if element with such value exists in the tree, otherwise returns False."""
        return self._find(value) is not None

    def insert(self, value):
        """Inserts element in the tree and returns True on success or False on failure."""
        if self.empty():  # empty tree, so value becomes the root
            self.root = Node(value)
            return True

        inserted = False  # insertion flag
        current = self.root  # start at the root
        while current.key != value:

            if value < current.key:

                if current.left is None:  # if no left child exists, insert element as left child
                    current.add_left(value=value)
                    inserted = True

                else:  # if a left child does exist, traverse left
                    current = current.left

            elif value > current.key:

                if current.right is None:  # if no right child exists, insert element as right child
                    current.add_right(value=value)
                    inserted = True

                else:  # if a right child does exist, traverse right
                    current = current.right

            if inserted:
                self._balance_tree(current=current)
                break

        return inserted  # failure to insert

    def remove(self, value):
        """Removes element with such value if it exists in the tree (returns True),
         or returns False otherwise."""
        current = self._find(value)
        if current is None:  # if no such value, failure
            return False

        # value is present in tree
        if current.left_child is None and current.right_child is None:  # case 1: no children
            current.parent.replace_child(current, None)

        elif current.left_child is not None and current.right_child is None:  # case 2: only left child
            current.parent.replace_child(current, current.left_child)

        elif current.left_child is None and current.right_child is not None:  # case 3: only right child
            current.parent.replace_child(current, current.right_child)

        else:  # case 4: two children
            successor = current.successor()
            # successor is the right child of current or the leftmost node in current's right subtree
            successor.parent.replace_child(successor, successor.right)
            current.value = successor.key

        return True

    def _min(self):
        """Returns minimum element in tree."""
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        """Return value of minimum element."""
        return self._min().key

    def _max(self):
        """Returns maximum element in tree."""
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def max(self):
        """Return value of maximum element."""
        return self._max().key

    def in_order(self):
        """In-order traversal over the values of the tree."""
        current = self._min()

        while current is not None:
            yield current.key
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
