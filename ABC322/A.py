n = int(input())
s = input()
bool = False
for i in range(n-2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
        bool = True
        print(i + 1)
        exit()

if not(bool):
    print(-1)