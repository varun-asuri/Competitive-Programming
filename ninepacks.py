from math import inf
h,b=[int(i) for i in input().split()[1:]],[int(i) for i in input().split()[1:]]
x,y=[inf]*(sum(h)+1),[inf]*(sum(b)+1)
x[0],y[0],a=0,0,inf
for t in h:
    for i in range(sum(h),-1,-1):
        if x[i]!=inf:x[i+t]=min(x[i+t],x[i]+1)
for t in b:
    for i in range(sum(b),-1,-1):
        if y[i]!=inf:y[i+t]=min(y[i+t],y[i]+1)
for i in range(1,min(sum(h)+1,sum(b)+1)):a=min(a,x[i]+y[i])
if a==inf:print('impossible')
else:print(a)