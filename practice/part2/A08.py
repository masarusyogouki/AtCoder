h, w = map(int, input().split())
X = [None] * h

for i in range(h):
    X[i] = list(map(int, input().split()))

q = int(input())
A = [None] * q
B = [None] * q
C = [None] * q
D = [None] * q
for j in range(q):
    A[j], B[j], C[j], D[j] = map(int, input().split())

#累積和
Z = [[0]* (w + 1) for _ in range(h + 1)]
#横方向に累積和を取る
for i in range(1, h+1):
    for j in range(1, w+1):
        Z[i][j] = Z[i][j-1] + X[i-1][j-1]

#縦方向に累積和を取る
for j in range(1, w+1):
    for i in range(1, h+1):
        Z[i][j] = Z[i-1][j] + Z[i][j]

for k in range(q):
    print(Z[C[k]][D[k]] + Z[A[k]-1][B[k]-1] - Z[A[k]-1][D[k]] - Z[C[k]][B[k]-1])