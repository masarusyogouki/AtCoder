d = int(input())
n = int(input())
L = [None] * n
R = [None] * n

for i in range(n):
    L[i], R[i] = map(int, input().split())

# 前日比
a = [0] * (d + 2)
for j in range(n):
    a[L[j]] += 1
    a[R[j]+1] -= 1

ans = [None] * (d + 2)
ans[0] = 0
for k in range(1, d+1):
    ans[k] = ans[k-1] + a[k]

for d in range(1, d+1):
    print(ans[d])