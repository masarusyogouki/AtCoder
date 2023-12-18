N , L, R = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < R and A[i] >= L:
        print(A[i], end=" ")
    elif A[i] < L:
        print(L, end=" ")
    else:
        print(R, end=" ")