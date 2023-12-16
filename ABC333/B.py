s = input()
s = list(s)
t = input()
t = list(t)

p = ["A", "B", "C", "D", "E"]

s_length = abs(p.index(s[1]) - p.index(s[0]))
t_length = abs(p.index(t[1]) - p.index(t[0]))


if s_length == t_length:
    print("Yes")
elif (s_length == 2 and t_length == 3) or (s_length == 3 and t_length == 2):
    print("Yes")
elif (s_length == 1 and t_length == 4) or (s_length == 4 and t_length == 1):
    print("Yes")
else:
    print("No")