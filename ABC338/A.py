s = list(input())
tb = s[0]
ta = "".join(s[1:])

if not(tb.islower()):
    tb = True
else:
    tb = False

if ta.islower():
    ta = True
elif len(s) == 1:
    ta = True
else:
    ta = False

if tb and ta:
    print("Yes")
else:
    print("No")