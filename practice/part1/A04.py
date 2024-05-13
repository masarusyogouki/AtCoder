n = int(input())
result = format(n, "b")
result = list(result)
while len(result) < 10:
    result.insert(0, '0')
    
for i in result:
    print(i, end='')