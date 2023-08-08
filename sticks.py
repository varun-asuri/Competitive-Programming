n,m=tuple(map(int,input().split()))
a,b={i:0 for i in range(1,n+1)},{i:[] for i in range(1,n+1)}
for i in range(m):
    x,y=tuple(map(int,input().split()))
    b[x].append(y)
    a[y]+=1
s=[]
for k in a:
    if a[k]==0: s.append(k)
p=[]
while s:
    t=s.pop()
    p.append(t)
    for i in b[t]:
        a[i]-=1
        if a[i]==0: s.append(i)
if len(p)==n: 
    for t in p: print(t)
else: print('IMPOSSIBLE')