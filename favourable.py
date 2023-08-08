def recur(x):
    if x in c:return c[x]
    if x==1:return 1
    if x in d:
        c[x]=sum([recur(k) for k in d[x]])
        return c[x]
    return 0
for i in range(int(input())):
    s,d,f,c=int(input()),{},[],{}
    for i in range(s):
        p=input().split()
        if len(p)==2:
            if p[1]=='favourably':f.append(int(p[0]))
        else:
            for j,x in enumerate(p):
                if j==0:continue
                if int(x) in d:d[int(x)].append(int(p[0]))
                else:d[int(x)]=[int(p[0])]
    print(sum([recur(i) for i in f]))