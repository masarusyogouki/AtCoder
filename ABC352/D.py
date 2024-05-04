n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = n

for i in range(1, n - k + 1):
    min = p.index(i)
    max = p.index(i)
    for j in range(1, k):
        tmp = p.index(i + j)
        if tmp < min:
            min = tmp
        elif tmp > max:
            max = tmp
    if ans > max - min:
        ans = max - min

print(ans)