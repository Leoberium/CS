import sys


class Heap:

    def __init__(self, a):
        self.a = a
        self.ops = []
        self.heapify()

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]
        self.ops.append((i, j))

    def sift_up(self, i):
        while i > 0 and self.a[self.parent(i)] > self.a[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def sift_down(self, i):
        index = i
        left = self.left_child(i)
        if left < len(self.a) and self.a[left] < self.a[index]:
            index = left
        right = self.right_child(i)
        if right < len(self.a) and self.a[right] < self.a[index]:
            index = right
        if index != i:
            self.swap(i, index)
            self.sift_down(index)

    def heapify(self):
        for i in range(len(self.a) - 1, -1, -1):
            self.sift_down(i)


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    h = Heap(a)
    print(len(h.ops))
    for i, j in h.ops:
        print(i, j)


if __name__ == '__main__':
    main()
