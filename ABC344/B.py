l = []
bool = True
while bool:
    a = int(input())
    l.append(a)
    if a == 0:
        bool = False

for i in range(len(l), 0, -1):
    print(l[i-1])