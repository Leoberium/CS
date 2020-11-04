import sys


class Tables:

    def __init__(self, size):
        self.size = size
        self.cur_max_size = max(size)
        self.par = [i for i in range(len(size))]
        self.rank = [0 for _ in range(len(size))]
        self.a = []

    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i, j):
        idi, idj = self.find(i - 1), self.find(j - 1)
        if idi == idj:
            self.a.append(self.cur_max_size)
            return
        if self.rank[idi] > self.rank[idj]:
            self.par[idj] = idi
            # updating size
            self.size[idi] += self.size[idj]
            if self.size[idi] > self.cur_max_size:
                self.cur_max_size = self.size[idi]
        else:
            self.par[idi] = idj
            # updating size
            self.size[idj] += self.size[idi]
            if self.size[idj] > self.cur_max_size:
                self.cur_max_size = self.size[idj]
            # updating rank
            if self.rank[idi] == self.rank[idj]:
                self.rank[idj] += 1
        self.a.append(self.cur_max_size)

    def output(self):
        for s in self.a:
            print(s)


def main():
    n, m = map(int, sys.stdin.readline().split())
    r = list(map(int, sys.stdin.readline().split()))
    t = Tables(r)
    for _ in range(m):
        t.union(*map(int, sys.stdin.readline().split()))
    t.output()


if __name__ == '__main__':
    main()
