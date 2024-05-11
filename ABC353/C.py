n = int(input())
a = list(map(int, input().split()))

t = 10 ** 8
ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        tmp = a[i] + a[j]
        if tmp >= t:
            ans += tmp - t
        else:
            ans += tmp

print(ans)

