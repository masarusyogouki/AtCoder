n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] == 1000:
                print('Yes')
                exit()

print('No')