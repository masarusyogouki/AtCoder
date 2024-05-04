s = list(map(int, input().split()))

n = s[0]
x = s[1]
y = s[2]
z = s[3]

c = 0
d = 0
if x > y:
    c = x
    d  = y
else:
    c = y
    d = x

if z > d and z < c:
    print("Yes")
else:
    print("No")
