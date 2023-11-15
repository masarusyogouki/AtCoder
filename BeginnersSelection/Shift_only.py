N = int(input())
L = list(map(int, input().split()))
cnt = 0
while all(i % 2 == 0 for i in L):
    L = [i / 2 for i in L]
    cnt += 1

print(cnt)
