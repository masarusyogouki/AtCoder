n = int(input())
a = list(map(int, input().split()))
n = 0
for i in a:
    n -= i
print(n)