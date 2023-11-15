N = int(input())
x, y = 0, 0
t = 0
bool = True
for i in range(N):
    t1, x1, y1 = map(int, input().split())
    time = t1 - t
    distance = abs(x1 - x) + abs(y1 - y)
    t = t1
    x = x1
    y = y1
    if time < distance or (time - distance) % 2 != 0:
        bool = False

if bool:
    print("Yes")
else:  
    print("No")