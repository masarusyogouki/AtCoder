s = list(input())
tmp = {}
for i in range(len(s)):
    if s[i] in tmp:
        tmp[s[i]] += 1
    else:
        tmp[s[i]] = 1

value_count = {}
for v in tmp.values():
    if v in value_count:
        value_count[v] += 1
    else:
        value_count[v] = 1

for v in value_count:
    if value_count[v] != 2:
        print("No")
        exit()

print("Yes")