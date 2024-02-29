h, w, n = map(int, input().split())
grid = []
steps = list(str(input()))
for i in range(h):
    grid.append(list(input()))

cnt = 0

def log(i, j, steps):
    for z in steps:
        if z == "L":
            if grid[i][j-1] == ".":
                j -= 1
        elif z == "R":
            if grid[i][j+1] == ".":
                j += 1
        elif z == "U":
            if grid[i-1][j] == ".":
                i -= 1
        elif z == "D":
            if grid[i+1][j] == ".":
                i += 1
        else:
            return False
    return True

for i in range(h):
    for j in range(w):
        start = grid[i][j]
        if start == "#":
            continue
        elif grid[i-1][j] == "." and grid[i+1][j] == "." and grid[i][j-1] == "." and grid[i][j+1] == ".":
            continue
        else:
            if log(i, j, steps):
                cnt += 1
print(cnt)