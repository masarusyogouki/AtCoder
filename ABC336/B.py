n = int(input())
cnt = 0
num = format(n, "b")
for i in range(len(num), 0, -1):
    if num[i - 1] == "0":
        cnt += 1
    else:
        break
print(cnt)