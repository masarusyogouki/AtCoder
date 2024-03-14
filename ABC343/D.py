import sys

n, t = map(int, sys.stdin.readline().split())
s = [0]* n
r = {0: n}

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    r[s[a -1]] -= 1
    if r[s[a -1]] == 0:
        r.pop(s[a -1])

    s[a -1] += b
    z = s[a -1]

    if r.get(z) == None:
        r[z] = 1
    else:
        r[z] += 1

    print(len(r))