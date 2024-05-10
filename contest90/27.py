n = int(input())
l = set()
for i in range(n):
    name = input()
    if name in l:
        continue
    else:
        l.add(name)
        print(i + 1)