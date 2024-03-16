n, m = map(int, input().split())
a = list(map(int, input().split()))
j = 0
for i in range(1, 1 + n):
    if i < a[j]:
        print(a[j] - i)
    if i == a[j]:
        j += 1
        print(0)