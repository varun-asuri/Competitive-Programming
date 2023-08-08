n,k=map(int,input().split())
t=[0]*(2*n)
def u(x):
 t[x+n],x=1-t[x+n],x+n
 x+=n
 while x>1:
  t[x>>1]=t[x]+t[x^1]
  x>>=1
def q(l,r):
 x,l,r=0,l+n,r+n
 while l<r:
  if l&1:x,l=x+t[l],l+1
  if r&1:x,r=x+t[r-1],r-1
  l,r=l>>1,r>>1
 return x
for k in range(k):
 s=input().split()
 if s[0]=='F':u(int(s[1])-1)
 else:print(q(int(s[1])-1,int(s[2])))