n, q = map(int, input().split())
a = list(map(int, input().split()))
L = [None] * q
R = [None] * q

for i in range(q):
    L[i], R[i] = map(int, input().split())

A = [None] * (n + 1)
A[0] = 0
for j in range(1,n+1):
    A[j] = A[j-1] + a[j-1]

for k in range(q):
    print(A[R[k]] - A[L[k]-1])