N = int(input())
A = list(map(int, input().split()))
B = list((i for i in A if i != max(A)))
print(max(B))