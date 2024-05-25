a, b = map(int, input().split())

l = [1,2,3]
if a in l:
    l.remove(a)
if b in l:
    l.remove(b)

if len(l) > 1:
    print(-1)
else:
    print(l[0])