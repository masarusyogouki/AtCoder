import math

a,b,c = map(int, input().split())
gcd = math.gcd(a,b,c)

ans = a // gcd - 1
ans += b // gcd - 1
ans += c // gcd - 1

print(ans)