s = input()
d = []
for i in range(1,len(s) + 1):
    for j in range(len(s) - i + 1):
        d.append(s[j:j + i])

print(len(set(d)))