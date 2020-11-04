import sys


class Variables:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i, j):
        ri, rj = self.find(i - 1), self.find(j - 1)
        if ri == rj:
            return
        if self.rank[ri] > self.rank[rj]:
            self.par[rj] = ri
        else:
            self.par[ri] = rj
            if self.rank[ri] == self.rank[rj]:
                self.rank[rj] += 1

    def are_disjoint(self, i, j):
        ri, rj = self.find(i - 1), self.find(j - 1)
        return 1 if ri != rj else 0


def main():
    n, e, d = map(int, sys.stdin.readline().split())
    v = Variables(n)
    for _ in range(e):
        v.union(*map(int, sys.stdin.readline().split()))
    r = 1
    for _ in range(d):
        r = v.are_disjoint(*map(int, sys.stdin.readline().split()))
        if r == 0:
            break
    print(r)


if __name__ == '__main__':
    main()
