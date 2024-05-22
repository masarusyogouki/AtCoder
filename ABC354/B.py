n = int(input())
t = 0
l = []

for _ in range(n):
    s, c = input().split()
    l.append((s, int(c)))
    t += int(c)

l = sorted(l)
ans = t % n
print(l[ans][0])