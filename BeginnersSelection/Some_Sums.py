N, A, B = map(int, input().split())
L = []
for i in range(1, N+1):
    L.append(i)
mom = 0
for i in L:
    j = list(map(int, str(i)))
    if sum(j) >= A and sum(j) <= B:
        mom += i
print(mom)