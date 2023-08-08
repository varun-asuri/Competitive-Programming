n,r,a=int(input()),[1]+[0]*2000,0
for x in [int(input())for i in range(n)]:
 for i in range(1000,-1,-1):
  if r[i]:
   r[i+x]=max(r[i],r[i+x])
   a=(a,i+x)[abs(i+x-1000.1)<abs(1000-a)]
print(a)