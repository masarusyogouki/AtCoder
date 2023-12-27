def check(n):
    s=str(n)
    c100=int(s[0])
    c10=int(s[1])
    c1=int(s[2])
    return c100*c10==c1

N=int(input())
for i in range(N,919+1):
    if check(i):
        print(i)
        exit()
