s = input()
message = "Yes"
for i in range(len(s)//2):
    if s[2*i - 1] == "1":
        message = "No"
        break

print(message)