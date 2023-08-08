m,q=tuple(map(int,input().split()))
b,s,l,p={},{},[],[]
for i in range(m):
    r=tuple(map(int,input().split()))
    l.append((r[1],r[2],r[0]))
l=sorted(l,reverse=True)
while l:
    x=l.pop()
    if p:
        while p and p[-1][1]<=x[1]:
            y=p.pop()
            b[y[2]],n=x[2],1
            if y[2] in s:n+=s[y[2]]
            if x[2] in s:s[x[2]]+=n
            else:s[x[2]]=n
    p.append(x)
for i in range(q):
    z=int(input())
    if z in b:print(b[z],end=' ')
    else:print(0,end=' ')
    if z in s:print(s[z])
    else:print(0)