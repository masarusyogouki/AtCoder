s = list(input())
target = s[0] if s[0] == s[1] else s[2]

for i in range(len(s)):
    if s[i] != target:
        print(i + 1)
        break