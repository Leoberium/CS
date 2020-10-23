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


def main():
    bst = []

    for _ in range(int(sys.stdin.readline())):
        # read node
        bst.append(tuple(map(int, sys.stdin.readline().split())))

    for order in traversals(bst):
        print(order)


if __name__ == '__main__':
    main()
