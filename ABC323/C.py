N, M = map(int,input().split())
A = list(map(int,input().split()))
S = [input() for _ in range(N)]
point = [i+1 for i in range(N)]
for i in range(N):
    for j in range(M):  
        if S[i][j] == 'o':
            point[i] += A[j]
mx = max(point)
for i in range(N):
    mikaiketsu = [A[j] for j in range(M) if S[i][j] == 'x']
    mikaiketsu.sort(reverse=True)
    ans = 0
    while point[i] < mx:
        point[i] += mikaiketsu[ans]
        ans += 1
    print(ans)