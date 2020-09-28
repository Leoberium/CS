"""I'm useful module."""
from .foo import *
from .bar import *

__all__ = foo.__all__ + bar.__all__

some_variable = "foobar"

print("useful.__init__.py")


def boo():
    return 42


def test():
    assert boo() == 4


if __name__ == "__main__":
    print("Running tests ...")
    test()
    print("OK")
