import sys


def height(parents, n):
    # iterative BFS solution
    tree = [[] for _ in range(n)]
    root = 0
    for v in range(n):
        u = parents[v]
        if u == -1:
            root = v
            continue
        tree[u].append(v)
    # BFS
    dist = [0] * n
    queue = [root]
    while queue:
        u = queue.pop(0)
        for v in tree[u]:
            dist[v] = dist[u] + 1
            queue.append(v)
    return max(dist) + 1


def main():
    n = int(sys.stdin.readline())
    p = list(map(int, input().split()))
    print(height(p, n))


if __name__ == '__main__':
    main()
