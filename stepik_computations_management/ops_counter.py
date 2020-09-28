n, v = map(int, input().split())
print(2 + n * (1 + v + v * (v - 1) // 2))
