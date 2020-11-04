import sys


p = 1000000007


def sh(s):
    return sum(ord(ch) for ch in s) % p


def kr(pattern, text):
    n, m = len(text), len(pattern)
    ph = sh(pattern)  # pattern hash
    a = []  # pattern occurrences
    # initial substring hash
    th = sh(text[:m])
    if th == ph and pattern == text[:m]:
        a.append(0)
    # sliding window
    for i in range(1, n - m + 1):
        th = (th - ord(text[i-1]) + ord(text[i+m-1])) % p
        if th == ph and pattern == text[i:i+m]:
            a.append(i)
    return a


def main():
    p = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(*kr(p, t))


if __name__ == '__main__':
    main()
