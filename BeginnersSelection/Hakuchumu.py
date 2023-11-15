L = ["dream","dreamer","erase", "eraser"]
S = str(input())
bool = False
for i in L:
    for j in L:
        if S == (i+j):
            bool = True
            print("YES")

if not bool:
    print("NO")