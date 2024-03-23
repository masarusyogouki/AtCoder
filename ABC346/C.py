n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
s = k*(k + 1)//2
for i in a:
    if i <= k:
        s -= i

print(s)