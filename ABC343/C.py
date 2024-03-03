n = int(input())

t = int(n ** (1/3)) + 1

for i in range(t, 0, -1):
    a = i ** 3
    if a <= n:
        r = list(str(a))
        z = True
        for j in range(len(r)//2):
            if r[j] != r[-j-1]:
                z = False
                break

        if z:
            print(a)
            exit()