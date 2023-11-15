B = int(input())

for A in range(1, 16):
    x = 1
    for i in range(A):
        x *= A
    if x == B:
        print(A)
        break
else:
    print(-1)