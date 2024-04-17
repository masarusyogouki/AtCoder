text = ""
for i in range(1, 101):
    if i % 3 == 0:
        text += "ZERO" * i
    elif i % 3 == 1:
        text += "ONE" * i
    else:
        text += "TWO" * i

a = []
for i in range(0, len(text), 1000):
    a.append(text[i:i+1000])


for i in range(len(a)):
    print(a[i][299], end = "")