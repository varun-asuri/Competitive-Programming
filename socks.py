i=input
s,c,k=map(int,i().split())
a,w,p,r=sorted(list(map(int,i().split()))),1,1,1
f=a[0]
while p<s:
 if r==c or a[p]-f>k:w,f,r=w+1,a[p],1
 else:r+=1
 p+=1
print(w)