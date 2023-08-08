e,u,w=[[1,4,5],[0,2,4,5,6],[1,3,5,6,7],[2,6,7],[0,1,5,8,9],[0,1,2,4,6,8,9,10],[1,2,3,5,7,9,10,11],[2,3,6,10,11],[4,5,9,12,13],[4,5,6,8,10,12,13,14],[5,6,7,9,11,13,14,15],[6,7,10,14,15],[8,9,13],[8,9,10,12,14],[9,10,11,13,15],[10,11,14]],[0,0,0,1,1,2,3,5,11],[]
for i in range(int(input())):w.append(input().rstrip())
input();t=int(input())
for m in range(t):
    d,b,p,y={},[*(input()+input()+input()+input())],[0,'',0],set()
    for i,r in enumerate(b):
        if r in d:d[r].append(i)
        else:d[r]=[i]
    v=[1]*16
    def f(g,h,a):
        if a in y:return 0
        v[h]=0
        if g==len(a):
            y.add(a)
            if g>len(p[1]) or g==len(p[1]) and a<p[1]:p[1]=a
            p[0],p[2]=p[0]+u[g],p[2]+1
            v[h]=1;return 1
        for k in e[h]:
            if b[k]==a[g] and v[k]:
                v[k]=0
                s=f(g+1,k,a)
                v[k]=1
                if s:return 1
        return 0
                
    for a in w:
        j=0
        for o in a:
            if o not in d: j=1
        if j or a in y:continue
        for i in d[a[0]]:
            v[i]=0
            f(1,i,a)
            v[i]=1
    print(p[0],p[1],p[2])
    if m<t-1:input()