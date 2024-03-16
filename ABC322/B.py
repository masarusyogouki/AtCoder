n, m = map(int, input().split())
s = input()
t = input()

head = t.startswith(s,0)
tail = t.endswith(s,0)

if head and tail:
    print(0)
elif head:
    print(1)
elif tail:
    print(2)
else:
    print(3)