import sys
from math import log2
from typing import Union

import hypothesis.strategies as st
from hypothesis import given, settings


class Node:
    """Node class for AVL tree. Implements many useful methods."""

    def __init__(self, key: int):
        # the node determines its subtree also
        self.key: int = key
        self.sum: int = self.key  # sum of keys in subtree
        self.height: int = 1  # height of subtree
        self.size: int = 1  # size of subtree
        self.balance_factor: int = 0
        self.parent: Union[Node, None] = None
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None

    def __repr__(self):
        return f"Node: key={self.key}, height={self.height}, balance_factor={self.balance_factor}, " \
               f"size={self.size}, sum={self.sum})"

    def __iter__(self):
        """In-order traversal of subtree."""
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right

    def __getitem__(self, item: int, base: int = 1) -> "Node":
        """Access element by index."""
        item += base ^ 1
        left_size = self.left.size if self.left is not None else 0
        if 0 < item < left_size + 1:
            return self.left.__getitem__(item)
        elif item == left_size + 1:
            return self
        elif left_size + 1 < item <= self.size:
            return self.right.__getitem__(item - left_size - 1)
        else:
            raise IndexError(f"Index out of range: {item - base ^ 1}")

    def __erase_links(self):
        self.parent = None
        self.left = None
        self.right = None

    def __update_height(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        self.height = 1 + max(left_height, right_height)
        self.balance_factor = right_height - left_height

    def __update_sum(self):
        left_sum = self.left.sum if self.left is not None else 0
        right_sum = self.right.sum if self.right is not None else 0
        self.sum = self.key + left_sum + right_sum

    def __update_size(self):
        left_size = self.left.size if self.left is not None else 0
        right_size = self.right.size if self.right is not None else 0
        self.size = 1 + left_size + right_size

    def __update_all(self):
        self.__update_height()
        self.__update_size()
        self.__update_sum()

    def __rotate_left(self) -> "Node":
        """Perform a left AVL rotation on the node. Returns new root of the subtree."""
        lower = self.right
        # add left subtree of lower to upper (self) as right child and update links
        self.right = lower.left
        if self.right is not None:
            self.right.parent = self
        self.__update_all()
        # update lower and upper links
        parent = self.parent
        lower.left = self
        self.parent = lower
        lower.__update_all()
        # update parent links
        lower.parent = parent
        if parent is not None and parent.left == self:
            parent.left = lower
        elif parent is not None and parent.right == self:
            parent.right = lower
        return lower  # new root of subtree

    def __rotate_right(self) -> "Node":
        """Perform a right AVL rotation on the node. Returns new root of the subtree."""
        lower = self.left
        # add right subtree of lower to upper (self) as left child and update links
        self.left = lower.right
        if self.left is not None:
            self.left.parent = self
        self.__update_all()
        # update lower and upper links
        parent = self.parent
        lower.right = self
        self.parent = lower
        lower.__update_all()
        # update parent links
        lower.parent = parent
        if parent is not None and parent.left == self:
            parent.left = lower
        elif parent is not None and parent.right == self:
            parent.right = lower
        return lower  # new root of subtree

    def __balance(self) -> "Node":
        """Balance tree starting from current node. Return root node of the whole tree."""
        current = self

        while True:
            current.__update_height()

            if current.balance_factor == 2:  # right subtree is higher
                middle = current.right
                if middle.balance_factor < 0:  # left subtree of middle node is higher
                    middle.__rotate_right()
                current = current.__rotate_left()

            elif current.balance_factor == -2:  # left subtree is higher
                middle = current.left
                if middle.balance_factor > 0:  # right subtree of middle node is higher
                    middle.__rotate_left()
                current = current.__rotate_right()

            else:
                current.__update_size()
                current.__update_sum()

            if current.parent is None:
                return current  # return root

            current = current.parent  # go up if not root

    def add_left(self, key: int) -> "Node":
        """Add left child, return new root. Raises an exception when such child exists."""
        if self.left is None:
            if key >= self.key:
                raise ValueError("Key isn't less than parent's key")
            self.left = Node(key=key)
            self.left.parent = self
        else:
            raise ValueError("Left child exists")
        return self.__balance()

    def add_right(self, key: int) -> "Node":
        """Add right child, return new root. Raises an exception when such child exists."""
        if self.right is None:
            if key <= self.key:
                raise ValueError("Key isn't bigger than parent's key")
            self.right = Node(key=key)
            self.right.parent = self
        else:
            raise ValueError("Right child exists")
        return self.__balance()

    def min(self) -> "Node":
        """Return element with minimal key in this subtree."""
        current = self
        while current.left is not None:
            current = current.left
        return current

    def max(self) -> "Node":
        """Return element with maximal key in this subtree."""
        current = self
        while current.right is not None:
            current = current.right
        return current

    def predecessor(self) -> Union["Node", None]:
        """Return element with previous key."""
        if self.left is not None:  # case 1: the node has a left child
            return self.left.max()

        else:  # case 2: the node does not have a left child
            current = self
            while current.parent is not None:  # traverse up
                if current == current.parent.right:
                    return current.parent
                else:
                    current = current.parent

            return None  # the root is reached, so no predecessor exists

    def successor(self) -> Union["Node", None]:
        """Return element with next key."""
        if self.right is not None:  # case 1: the node has a right child
            return self.right.min()

        else:  # case 2: the node does not have a right child
            current = self
            while current.parent is not None:  # traverse up
                if current == current.parent.left:
                    return current.parent
                else:
                    current = current.parent

            return None  # the root is reached, so no successor exists

    def find(self, key) -> Union["Node", None]:
        """Return element with such key if present, otherwise None."""
        current = self
        while key != current.key:
            if key < current.key:
                current = current.left  # traverse left

            elif key > current.key:
                current = current.right  # traverse right

            if current is None:  # failure
                break
        return current

    def remove(self):
        """Remove element from the tree, update links of adjacent nodes."""
        parent = self.parent
        if self.left is None and self.right is None:  # case 1: no children

            if parent is None:
                return None  # remove root
            elif parent.left is self:
                parent.left = None  # remove left leaf
            elif parent.right is self:
                parent.right = None  # remove right leaf

        elif self.left is not None and self.right is None:  # case 2: left child
            left = self.left
            left.parent = parent
            self.left = None

            if parent is None:
                return left  # left is new root
            elif parent.left is self:
                parent.left = left  # update left leaf
            elif parent.right is self:
                parent.right = left  # update right leaf

        elif self.left is None and self.right is not None:  # case 3: right child
            right = self.right
            right.parent = parent
            self.right = None

            if parent is None:
                return right  # right is new root
            elif parent.left is self:
                parent.left = right  # update left leaf
            elif parent.right is self:
                parent.right = right  # update right leaf

        else:  # case 4: both child
            successor = self.successor()
            self.key = successor.key  # exchange keys
            return successor.remove()  # remove successor leaf

        self.parent = None  # remove last link from the node
        return parent.__balance()


class AVLTree:

    def __init__(self, root=None):
        self.root: Union[Node, None] = root

    def __iter__(self):
        """In-order traversal of the tree."""
        if self.empty():
            return
        for node in self.root:
            yield node.key

    def __getitem__(self, item: int) -> int:
        """Get key by index."""
        return self.root[item].key

    def empty(self) -> bool:
        """Check if the tree is empty."""
        return True if self.root is None else False

    @property
    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return self.root.size if not self.empty() else 0

    @property
    def height(self) -> int:
        """Return the height of the tree."""
        return self.root.height if not self.empty() else 0

    def clear(self):
        """Clear the tree."""
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

    def find(self, key: int) -> bool:
        """Return True if element with such key exists in the tree, otherwise False."""
        return self.root.find(key) is not None

    def insert(self, key: int) -> bool:
        """Insert key (create new element) in the tree
         and return True on success or False on failure."""
        if self.empty():  # empty tree, so value becomes the root
            self.root = Node(key)
            return True

        current = self.root  # start at the root
        while current.key != key:

            if key < current.key:

                if current.left is None:  # if no left child exists, insert element as left child
                    self.root = current.add_left(key=key)
                    return True

                else:  # if a left child does exist, traverse left
                    current = current.left

            elif key > current.key:

                if current.right is None:  # if no right child exists, insert element as right child
                    self.root = current.add_right(key=key)
                    return True

                else:  # if a right child does exist, traverse right
                    current = current.right

        return False  # failure to insert

    def remove(self, key: int) -> bool:
        """Remove element with such key if it exists in the tree (return True),
         or return False otherwise."""
        current = self.root.find(key)
        if current is None:  # if no such key, failure
            return False

        self.root = current.remove()  # update root
        return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        op, *args = sys.stdin.readline().strip().split(" ")


@given(st.lists(
    st.integers(min_value=-10000, max_value=10000),
    max_size=10000, unique=True))
@settings(max_examples=250)
def test_bst_properties(seq):
    tree = AVLTree()
    for x in seq:
        tree.insert(x)
    assert list(tree) == sorted(seq)
    assert tree.size == len(seq)
    assert tree.height <= 1.44 * log2(1 + len(seq))
    if len(seq) >= 10:
        assert tree.find(seq[5])
        assert tree.find(seq[3])
        assert tree.find(25) == (25 in seq)
        assert tree.remove(seq.pop())
        assert list(tree) == sorted(seq)
        assert tree.remove(seq.pop())
        assert list(tree) == sorted(seq)
        assert tree.size == len(seq)
        assert tree.find(seq[5])
        assert tree.remove(seq.pop(len(seq) // 2))
        assert list(tree) == sorted(seq)
