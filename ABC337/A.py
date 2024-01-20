n = int(input())
x, y = 0, 0
for i in range(n):
    a,b = map(int, input().split())
    x += a
    y += b

if x > y:
    print("Takahashi")
elif x == y:
    print("Draw")
else:
    print("Aoki")