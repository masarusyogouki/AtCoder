N = int(input())  # 月の数

count = 0  # ゾロ目の日付のカウンター

for i in range(1, N + 1):
    Di = int(input())  # 月の日数
    for j in range(1, Di + 1):
        ij_str = str(i) + str(j)
        if len(set(ij_str)) == 1:
            count += 1

print(count)
