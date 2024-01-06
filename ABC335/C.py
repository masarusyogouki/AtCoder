n, q = map(int, input().split())
p = [[n-i,0] for i in range(n)]
now = (1,0)
for _ in range(q):
    a, b = input().split()
    if a == "1":
        if b=="U":
            nxt = (now[0],now[1]+1)
        elif b=="D":
            nxt = (now[0],now[1]-1)
        elif b=="L":
            nxt = (now[0]-1,now[1])
        else:
            nxt = (now[0]+1,now[1])
        p.append(nxt)
        now = nxt
    else:
        print(p[int(b)*-1][0],p[int(b)*-1][1])