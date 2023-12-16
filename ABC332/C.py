n, m = map(int, input().split())
s = input() + "0"

max_score, x, y = 0, 0, 0

for i in range(len(s)):
    if s[i] == '0':
        max_score = max(max_score, max(x + y - m, y))
        x, y = 0, 0
    elif s[i] == '1':
        x += 1
    elif s[i] == '2':
        y += 1

print(max_score)
