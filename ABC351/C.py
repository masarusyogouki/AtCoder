n = int(input())
a = list(map(int, input().split()))

s = list()

def f(x):
    if len(x) == 1:
        return
    if x[-1] == x[-2]:
        s.append(x[-1] + 1)
        s.pop(-2)
        s.pop(-2)
        return f(s)
    else:
        return

for i in range(n):
    s.append(a[i])
    f(s)

print(len(s))