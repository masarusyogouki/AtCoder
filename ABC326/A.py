x, y = map(int, input().split())

if x - y == 3:
    print("Yes")
elif y - x == 2:
    print("Yes")
else:  
    print("No")