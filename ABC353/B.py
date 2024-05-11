
n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
m = k

for i in a:
    if m - i >= 0:
        m -= i
    else:
        cnt += 1
        m = k - i


print(cnt + 1)