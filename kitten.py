k,d,l=int(input()),{},input().rstrip()
while l!="-1":
    l=list(map(int,l.split()))
    for i in range(1,len(l)):d[l[i]]=l[0]
    l=input().rstrip()
print(k,end='')
while k in d:
    print(' ',d[k],sep='',end='')
    k=d[k]