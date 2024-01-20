n = int(input())
A = list(map(int, input().split()))
B = []
B[0] = A.index(-1) + 1
for i in range(1, n):
    B[i] = A.index(B[i-1]) + 1

print(*B)