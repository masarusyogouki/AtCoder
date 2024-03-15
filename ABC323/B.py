n = int(input())
players = [input() for i in range(n)]
score = {i: 0 for i in range(n)}
for i in range(n):
    cnt = 0
    for j in range(n):
        if players[i][j] == "o":
            cnt += 1
    score[i] = cnt
score = sorted(score.items(), key=lambda x: x[1], reverse=True)
for key, value in score:
    print(key + 1, end = " ")