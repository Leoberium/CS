import sys


def balanced(s):
    stack = []
    d = {']': '[', '}': '{', ')': '('}
    for i in range(len(s)):
        ch = s[i]
        if ch in '[({':
            stack.append(i)
        elif ch in '])}':
            if stack:
                if s[stack[-1]] == d[ch]:
                    stack.pop()
                else:
                    # no match
                    return i + 1
            else:
                # empty stack
                return i + 1
    # if stack is not empty - return position of the first element
    return 'Success' if not stack else stack[0] + 1


def main():
    s = sys.stdin.readline().strip()
    print(balanced(s))


if __name__ == '__main__':
    main()
