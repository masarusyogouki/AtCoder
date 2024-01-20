n = int(input())
A = list(map(int, input().split()))
B = []
d = {}
for i in range(n):
    if A[i] == -1:
        B.append(i+1)
    else:
        B.append(d[A[i]]+1)
    d[A[i]] = i
print(*B)
