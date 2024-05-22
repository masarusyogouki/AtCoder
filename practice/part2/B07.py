t = int(input())
n = int(input())
a = [0] * (t+1)

L = [None] * n
R = [None] * n

for i in range(n):
    L[i], R[i] = map(int, input().split())

for j in range(n):
    a[L[j]] += 1
    a[R[j]] -= 1

b = [0] * (t+1)
b[0] = a[0]
for k in range(1, t+1):
    b[k] = b[k-1] + a[k]

for l in range(t):
    print(b[l])