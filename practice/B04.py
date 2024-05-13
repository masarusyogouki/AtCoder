n = input()
a = list(reversed(n))
ans = 0

for i in range(len(a)):
    if a[i] == "1":
        ans += 2**i

print(ans)