N = int(input())
L = []
for _ in range(N):
    d = int(input())
    L.append(d)
L_sort = sorted(L, reverse=True)
cnt = 1
for i in range(N-1):
    if L_sort[i] > L_sort[i+1]:
        cnt += 1

print(cnt)