import useful
import sys


def main():
    print(dir(useful))
    print(useful.__name__)
    print(useful.__doc__)
    print(useful.__file__)
    print(useful.__cached__)
    print(sys.path)


if __name__ == '__main__':
    main()
