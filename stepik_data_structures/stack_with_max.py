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
            self.s.pop()
            self.m.pop()
            if self.m:
                self.cur_max = self.m[-1]
            else:
                self.cur_max = minus_inf
        else:
            return ''

    def operation(self, s):
        if s[-1].isdigit():
            p, v = s.split()
            self.push(int(v))
        else:
            if s == 'max':
                print(self.cur_max)
            else:
                self.pop()


def main():
    n = int(sys.stdin.readline().strip())
    s = Stack()
    for _ in range(n):
        line = sys.stdin.readline().strip()
        s.operation(line)


if __name__ == '__main__':
    main()
