import sys

n, a, b = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

r = [i % (a + b) for i in d]
z = [range(a, a + b)]

if 0 or z in r:
    print("No")
    sys.exit()

print("Yes")