n,k=tuple(map(int,input().split()))
s=[]
t=0
for i in input():
    if i==' ':s.append(t);t=0
    else:t=t*10+int(i)
s.append(t)
s=sorted(s,reverse=True)
p,l,h,v,a,d={},{},{},set(),0,0
e=[(int(input()),i) for i in range(1,n)][::-1]
e.append((-1,0))
for f,i in e:
    if f!=-1:
        p[i]=f
        if f in l:l[f].append(i)
        else:l[f]=[i]
    if i not in h:h[i]=(0,i)
    if i in l:
        u=[]
        for x in l[i]:
            if h[x][0]+1>h[i][0]:
                h[i]=(h[x][0]+1,h[x][1])
                if u:
                    v.remove(u[-1])
                    u.pop()
                v.add(x)
                u.append(x)
b=sorted([(h[i][0],i) for i in h])
while b:
    x=b.pop()
    if x[1] in v:continue
    v.add(x[1])
    a+=(x[0]+1)*s[d]
    d+=1
print(a-s[0])