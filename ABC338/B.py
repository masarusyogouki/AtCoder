s = list(input())
d = {}
for str in s:
    if str in d:
        d[str] += 1
    else:
        d[str] = 1

max_value = max(d.values())
max_key = [k for k, v in d.items() if v == max_value]
print(sorted(max_key)[0])