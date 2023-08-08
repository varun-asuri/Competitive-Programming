n,c,f,s,t,m=int(input()),0,0,[],0,[]
for i in range(n):
    x=list(map(int,input().split()))
    x.append(sum(x[1:]))
    t+=x[0]
    if x[1]>x[4]/2:c+=x[0]
    elif x[2]>=x[4]/2:f+=x[0]
    else:m.append(i);x.append(x[-1]//2-x[1]+1)
    s.append(x)
if c>t/2:print(0)
elif f>=t/2:print("impossible")
else:
    d=[10**10]*(t//2+2-c)
    d[0]=0
    for i in range(len(m)):
        for j in range(len(d)-2,-1,-1):
            if d[j]<10**10:
                x=j+s[m[i]][0]
                y=d[j]+s[m[i]][-1]
                d[x]=min(d[x],y)
    x=-1
    for i in range(t//2+1-c,len(d)):
        if x==-1:x=d[i]
        else:x=min(x,d[i])
    print(x)