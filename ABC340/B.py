q = int(input())
query = []

for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        query.append(b)
    else:
        print(query[-b])