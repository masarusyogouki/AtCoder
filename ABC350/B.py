n, q = map(int, input().split())
t = list(map(int, input().split()))

d = [1]*n
cnt = n

for i in t:
    if d[i - 1] == 1:
        d[i - 1] = 0
        cnt -= 1
    else:
        d[i - 1] = 1
        cnt += 1

print(cnt)