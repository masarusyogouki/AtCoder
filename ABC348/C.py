n = int(input())
a = {}

for _ in range(n):
    v, k = map(int, input().split())
    if k in a:
        if a[k] > v:
            a[k] = v
    else:
        a[k] = v

print(max(a.values()))