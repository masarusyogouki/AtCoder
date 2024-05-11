n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    if a[i] > a[0]:
        print(i + 1)
        exit()

print(-1)