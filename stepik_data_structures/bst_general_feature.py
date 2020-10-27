import sys


def check_general_feature(bst: list):
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
            # compare if current has left subtree
            if bst[current][1] != -1 and key_previous >= bst[current][0]:
                return "INCORRECT"
            # compare if current has no left subtree
            elif bst[current][1] == -1 and key_previous > bst[current][0]:
                return "INCORRECT"
            key_previous = bst[current][0]  # update previous key
            current = bst[current][2]  # right child

        else:
            break

    return "CORRECT"


if __name__ == '__main__':
    t = []
    for _ in range(int(sys.stdin.readline())):
        t.append(tuple(map(int, sys.stdin.readline().split())))
    print(check_general_feature(t))


def test_check_general_feature():
    assert check_general_feature([]) == "CORRECT"
    assert check_general_feature([
        (2, 1, 2),
        (1, -1, -1),
        (3, -1, -1)
    ]) == "CORRECT"
    assert check_general_feature([
        (1, 1, 2),
        (2, -1, -1),
        (3, -1, -1)
    ]) == "INCORRECT"
    assert check_general_feature([
        (2, 1, 2),
        (1, -1, -1),
        (2, -1, -1)
    ]) == "CORRECT"
    assert check_general_feature([
        (2, 1, 2),
        (2, -1, -1),
        (3, -1, -1)
    ]) == "INCORRECT"
    assert check_general_feature([
        (2147483647, -1, -1)
    ]) == "CORRECT"
    assert check_general_feature([
        (1, -1, 1),
        (2, -1, 2),
        (3, -1, 3),
        (4, -1, 4),
        (5, -1, -1)
    ]) == "CORRECT"
    assert check_general_feature([
        (4, 1, 2),
        (2, 3, 4),
        (6, 5, 6),
        (1, -1, -1),
        (3, -1, -1),
        (5, -1, -1),
        (7, -1, -1)
    ]) == "CORRECT"
