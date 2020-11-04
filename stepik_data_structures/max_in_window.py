import sys


minus_inf = -float('inf')


class Stack:

    def __init__(self):
        self.s = []  # element stack
        self.m = []  # max element stack
        self.cur_max = minus_inf

    def empty(self):
        if not self.s or not self.m:
            return True
        return False

    def push(self, value):
        self.s.append(value)
        if value > self.cur_max:
            self.cur_max = value
        self.m.append(self.cur_max)

    def pop(self):
        if not self.empty():
            n = self.s.pop()
            self.m.pop()
            if self.m:
                self.cur_max = self.m[-1]
            else:
                self.cur_max = minus_inf
            return n
        return None

    def max(self):
        return self.cur_max


def max_in_window(a, m):
    s = []  # all max
    # initialization
    left, right = Stack(), Stack()  # two stacks with max support
    for i in range(m):
        left.push(a[i])
    while not left.empty():
        right.push(left.pop())
    s.append(right.max())
    # sliding a window
    for i in range(m, len(a)):
        right.pop()
        left.push(a[i])
        if right.empty():
            while not left.empty():
                right.push(left.pop())
        if right.max() > left.max():
            s.append(right.max())
        else:
            s.append(left.max())
    return s


def main():
    sys.stdin.readline()
    a = list(map(int , sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    print(*max_in_window(a, m))


if __name__ == '__main__':
    main()
