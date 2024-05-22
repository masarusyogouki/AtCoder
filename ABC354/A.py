n = int(input())
tmp = 0
ans = 0

while tmp + 2** ans <= n:
    tmp += 2**ans
    ans += 1

print(ans + 1)