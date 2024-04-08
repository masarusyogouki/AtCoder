n = int(input())
for i in range(n):
    i += 1
    if i % 3 == 0:
        print("x", end="")
    else:
        print("o", end="")