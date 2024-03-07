n = int(input())

def cal(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        n = n // 2
        return cal(n)
    elif n % 3 == 0:
        n = n // 3
        return cal(n)
    else:
        return False
    
if cal(n):
    print("Yes")
else:
    print("No")