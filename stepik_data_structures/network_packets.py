import sys


class Processor:

    def __init__(self, size, n):
        self.times = [(-1, -1)] * n
        self.free = size
        self.queue = []
        self.cnt = 0

    def add_packet(self, a, d):
        time = a
        while self.queue and self.times[self.queue[0]][1] <= a:
            self.queue.pop(0)
            self.free += 1
        if self.queue:
            time = self.times[self.queue[-1]][1]

        if self.free:
            self.free -= 1
            self.times[self.cnt] = (time, time + d)
            self.queue.append(self.cnt)
        self.cnt += 1

    def output(self):
        for start, end in self.times:
            print(start)


def main():
    size, n = map(int, sys.stdin.readline().split())
    p = Processor(size, n)
    for _ in range(n):
        arrival, duration = map(int, sys.stdin.readline().split())
        p.add_packet(arrival, duration)
    p.output()


if __name__ == '__main__':
    main()
