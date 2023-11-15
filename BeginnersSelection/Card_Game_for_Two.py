N = int(input())
A = list(map(int, input().split()))
A_sort = sorted(A, reverse=True)
num = 0
for i in range(N):
    if i % 2 == 0:
        num += A_sort[i]
    else:
        num -= A_sort[i]
print(num)