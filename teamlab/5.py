sum = 0
cnt = 0

for i in range(700, 0, -1):
    if sum + i> 5000:
        cnt += 1
        sum = i
    else:
        sum += i

cnt += 1 

print(cnt)