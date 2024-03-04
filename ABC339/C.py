n = int(input())
a = list(map(int, input().split()))
get = 0

for num in a:
    get += num
    if get < 0:
        get = 0

print(get)