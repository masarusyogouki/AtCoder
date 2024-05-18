d = int(input())
n = int(input())
l = [None] * n
r = [None] * n

for i in range(n):
    l[i], r[i] = map(int, input().split())

b = [0] * (d + 2)
for i in range(n):
    b[l[i]] += 1
    b[r[i] + 1] -= 1

ans = [0] * (d + 2)
ans[0] = 0

for d in range(1, d + 1):
    ans[d] = ans[d - 1] + b[d]

for d in range(1, d + 1):
    print(ans[d])