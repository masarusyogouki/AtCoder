s = input()
s = list(s)
bar = 0

for i in range(len(s)):
    if s[i] == "|":
        bar += 1
    else:
        if bar == 0:
            print(s[i], end="")
        elif bar == 1:
            print(end="")
        else:
            print(s[i], end="")