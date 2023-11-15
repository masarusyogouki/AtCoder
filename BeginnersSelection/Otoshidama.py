N, Y = map(int, input().split())
A = Y / 10000
B = Y / 5000
C = Y / 1000
l = []
bool = False
for a in range(int(A+1)):
    for b in range(int(B+1)):
        c = N - a - b
        if c >= 0 and 10000 * a + 5000 * b + 1000 * c == Y:
            l.append([a, b, c])
            bool = True

if bool:
    print(l[0][0], l[0][1], l[0][2])
else:
    print(-1, -1, -1)
