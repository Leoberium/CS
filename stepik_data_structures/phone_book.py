import sys


class PhoneBook:

    def __init__(self):
        self.a = [{} for _ in range(1000)]

    @staticmethod
    def hash(number):
        return number % 1000

    def add(self, number, name):
        self.a[self.hash(number)][number] = name

    def remove(self, number):
        h = self.hash(number)
        if number in self.a[h]:
            self.a[h].pop(number)

    def find(self, number):
        h = self.hash(number)
        if number in self.a[h]:
            print(self.a[h][number])
        else:
            print('not found')

    def op(self, s):
        s = s.split()
        if s[0] == 'add':
            self.add(int(s[1]), s[2])
        elif s[0] == 'find':
            self.find(int(s[1]))
        else:
            self.remove(int(s[1]))


def main():
    pb = PhoneBook()
    for _ in range(int(sys.stdin.readline())):
        pb.op(sys.stdin.readline().strip())


if __name__ == '__main__':
    main()
