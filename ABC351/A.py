a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in a:
    s += i

for j in b:
    s -= j

print(s + 1)