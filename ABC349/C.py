s = input()
t = input().lower()

tmp = 0

for i in range(3):
    if t[i] in s[tmp:]:
        tmp  = s[tmp:].index(t[i])
        if i == 2:
            print("Yes")
    else:
        if i == 2 and t[i] == "x":
            print("Yes")
        else:
            print("No")
            exit()