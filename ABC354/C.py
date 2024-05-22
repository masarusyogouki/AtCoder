n = int(input())

s = []

for i in range(n):
    a, c = map(int, input().split())
    s.append([c, a, i+1])

s.sort(reverse=True)

print(s)