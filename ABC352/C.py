n = int(input())

s = 0
z = 0
for _ in range(n):
    a, b = map(int, input().split())
    s += a
    if b - a > z:
        z = b - a

print(s + z)