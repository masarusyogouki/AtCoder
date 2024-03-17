s = input()
left = 0
right = 0

for i in range(len(s)):
    if s[i] == "<":
        left += 1
    if s[i] == ">":
        right += 1

if not(left == 1):
    print("No")
elif not(right == 1):
    print("No")
else:
    print("Yes")