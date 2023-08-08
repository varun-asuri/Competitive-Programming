from bisect import bisect_right as br
n=int(input())
a,b,c,d=map(int,input().split())
l,x,y=list(tuple(map(int, input().split())) for i in range(n)),1,1
if a>c:a,c,x=-a,-c,-1
if b>d:b,d,y=-b,-d,-1
p,e=sorted([(t[0]*x,t[1]*y) for t in l if a<=t[0]*x<=c and b<=t[1]*y<=d]),[]
for x in p:
    i=br(e,x[1])
    e.append('')
    e[i]=x[1]
    if e[-1]=='':e.pop()
print(len(e))