s = input()
t = input()

a = -1

for i in range(len(s)):
    for j in range(a + 1 , len(t)):
        if t[j] == s[i]:
            print(j + 1, end = " ")
            a = j
            break