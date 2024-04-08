n = int(input())
m = []
for _ in range(n):
    x, y = map(int, input().split())
    m.append((x, y))

for i in range(n):
    ans = 0
    tmp = 0
    for j in range(n):
        dist = (m[j][0]-m[i][0])**2 + (m[j][1]-m[i][1])**2
        if dist > ans:
            ans = dist
            tmp = j + 1
    print(tmp)