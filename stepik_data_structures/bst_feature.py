import sys


def check_feature(bst: list):
    if not bst:
        return "CORRECT"
    stack = []
    current = 0  # root
    key_previous = -sys.maxsize - 1

    while True:

        if current != -1:
            stack.append(current)
            current = bst[current][1]  # left child

        elif stack:
            current = stack.pop()
            if key_previous >= bst[current][0]:  # compare keys
                return "INCORRECT"
            key_previous = bst[current][0]  # update previous key
            current = bst[current][2]  # right child

        else:
            break

    return "CORRECT"


def main():
    bst = []
    for _ in range(int(sys.stdin.readline())):
        bst.append(tuple(map(int, sys.stdin.readline().split())))
    print(check_feature(bst))


if __name__ == '__main__':
    main()
