M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d + 1 > D:
    m += 1
    d = 1
else:
    d += 1

if m > M:
    y += 1
    m = 1

print(y,m,d)