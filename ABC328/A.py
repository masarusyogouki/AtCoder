N, X = map(int,input().split())
S = list(map(int, input().split()))
n = 0
for i in range(N):
    if S[i] <= X:
        n += S[i]

print(n)