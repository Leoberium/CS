import sys


def traversals(bst: list):
    pre_order, in_order, post_order = [], [], []

    # fill order lists recursively
    def dfs(v: int):

        if v == -1:
            return

        pre_order.append(bst[v][0])

        dfs(bst[v][1])

        in_order.append(bst[v][0])

        dfs(bst[v][2])

        post_order.append(bst[v][0])

    if bst:
        dfs(0)

    return in_order, pre_order, post_order


if __name__ == '__main__':
    t = []

    for _ in range(int(sys.stdin.readline())):
        # read node
        t.append(tuple(map(int, sys.stdin.readline().split())))

    for order in traversals(t):
        print(order)


def test_traversals():
    assert traversals([]) == ([], [], [])
    input1 = [
        (4, 1, 2),
        (2, 3, 4),
        (5, -1, -1),
        (1, - 1, - 1),
        (3, - 1, - 1)
    ]
    assert traversals(input1) == (
        [1, 2, 3, 4, 5],
        [4, 2, 1, 3, 5],
        [1, 3, 2, 5, 4]
    )
    input2 = [
        (0, 7, 2),
        (10, -1, -1),
        (20, -1, 6),
        (30, 8, 9),
        (40, 3, -1),
        (50, -1, -1),
        (60, 1, -1),
        (70, 5, 4),
        (80, -1, -1),
        (90, -1, -1)
    ]
    assert traversals(input2) == (
        [50, 70, 80, 30, 90, 40, 0, 20, 10, 60],
        [0, 70, 50, 40, 30, 80, 90, 20, 60, 10],
        [50, 80, 90, 30, 40, 70, 10, 60, 20, 0]
    )
