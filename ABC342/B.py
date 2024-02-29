n = int(input())
p = input().split()
q = int(input())

for _ in range(q):
    a, b = map(str, input().split())
    if p.index(a) > p.index(b):
        print(b)      
    else:
        print(a)