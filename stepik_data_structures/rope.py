import sys


def process(string, query):
    i, j, k = query
    insertion = string[i:j+1]
    tmp = string[:i] + string[j+1:]
    return tmp[:k] + insertion + tmp[k:]


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    for _ in range(int(sys.stdin.readline())):
        q = map(int, sys.stdin.readline().strip().split())
        s = process(s, q)
    print(s)


def test_rope():
    assert process("hlelowrold", (1, 1, 2)) == "hellowrold"
    assert process("hellowrold", (6, 6, 7)) == "helloworld"
    assert process("abcdef", (0, 1, 1)) == "cabdef"
    assert process("cabdef", (4, 5, 0)) == "efcabd"
