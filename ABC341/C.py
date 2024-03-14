h,w,n=map(int,input().split())
t=input()
s=[input()for _ in range(h)]
ans=0
for ni in range(h):
  for nj in range(w):
    if s[ni][nj]=='#':
      continue
    ok=1
    i,j=ni,nj
    for l in t:
      if l=='L':
        j-=1
      if l=='R':
        j+=1
      if l=='U':
        i-=1
      if l=='D':
        i+=1
      if s[i][j]=='#':
        ok=0
        break
    ans+=ok
print(ans)