s = list(input())
t = 0

for i in range(len(s)-1,0,-1):
    if s[i] == ".":
        t = i
        break

for j in range(t+1,len(s),1):
    print(s[j],end="")