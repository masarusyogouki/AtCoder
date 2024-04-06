n, k = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in a :
    f = i % k
    if f == 0:
        b.append(i // k)

for j in b:
    print(j, end = " ")
