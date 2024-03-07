n = int(input())
a = list(map(int, input().split()))
bool = "Yes"
for i in range(1,n):
    if a[0] != a[i]:
        bool = "No"
        break

print(bool)