n, t = map(int, input().split())
a = list(map(lambda x: int(x) -1, input().split()))
row = [0] * n
col = [0] * n
diag = [0] * 2

for i in range(t):
    x = a[i] // n
    y = a[i] % n 

    row[x] += 1
    if row[x] == n:
        print(i + 1)
        exit()
    
    col[y] += 1
    if col[y] == n:
        print(i + 1)
        exit()

    if x == y:
        diag[0] += 1
        if diag[0] == n:
            print(i + 1)
            exit()
    
    if x + y == n - 1:
        diag[1] += 1
        if diag[1] == n:
            print(i + 1)
            exit()

print(-1)