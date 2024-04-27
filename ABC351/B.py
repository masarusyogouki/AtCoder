n = int(input())

a = []
for i in range(n):
    s = input()
    a.append(s)

b = []
for j in range(n):
    s = input()
    b.append(s)

for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            print(i+1, j+1)
            exit()