n = int(input())
a = list(map(int, input().split()))
q = int(input())
L = [None] * q
R = [None] * q

for i in range(q):
    L[i], R[i] = map(int, input().split())

b = [None] * (n + 1)
b[0] = 0

for j in range(1, n+1):
    b[j] = b[j-1] + a[j-1]

for k in range(q):
    tmp = b[R[k]] - b[L[k] -1]
    day = (R[k] - L[k] + 1) / 2
    if tmp > day:
        print("win")
    elif tmp == day:
        print("draw")
    else:
        print("lose")