def count(n, a, cnt):
    t = a
    for i in range(n):
        if t[i] % 2 == 0:
            t[i] /= 2
    return cnt

n = int(input())
a = list(map(int, input().split()))
print(count(n, a, 0))
