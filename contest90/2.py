h, w = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]

row_sum = []
column_sum = [0] * w

for a in matrix:
    row_sum.append(sum(a))
    for i in range(w):
        column_sum[i] += a[i]

for h in range(h):
    q = []
    for w in range(w):
        q.append(row_sum[h] + column_sum[w] - matrix[h][w])
    print(*q)