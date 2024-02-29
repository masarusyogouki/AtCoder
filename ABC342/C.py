n = int(input())
s = input()
q = int(input())

trans_from = "abcdefghijklmnopqrstuvwxyz"
trans_to = "abcdefghijklmnopqrstuvwxyz"

for _ in range(q):
    c, d = map(str, input().split())
    trans_to = trans_to.replace(c, d)

print(s.translate(str.maketrans(trans_from, trans_to)))