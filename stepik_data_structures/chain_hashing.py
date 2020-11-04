import sys

p = 1000000007
x = 263


class Table:

    def __init__(self, m):
        self.m = m
        self.a = [[] for _ in range(m)]

    def sh(self, s):
        return sum(ord(s[i]) * x**i for i in range(len(s))) % p % self.m

    def add(self, s):
        h = self.sh(s)
        if s not in self.a[h]:
            self.a[h].append(s)

    def remove(self, s):
        h = self.sh(s)
        if s in self.a[h]:
            self.a[h].remove(s)

    def find(self, s):
        h = self.sh(s)
        if s in self.a[h]:
            print('yes')
        else:
            print('no')

    def check(self, i):
        print(*self.a[i][::-1])

    def op(self, o):
        o = o.split()
        if o[0] == 'add':
            self.add(o[1])
        elif o[0] == 'del':
            self.remove(o[1])
        elif o[0] == 'find':
            self.find(o[1])
        else:
            self.check(int(o[1]))


def main():
    m = int(sys.stdin.readline())
    t = Table(m)
    for _ in range(int(sys.stdin.readline())):
        t.op(sys.stdin.readline().strip())


if __name__ == '__main__':
    main()
