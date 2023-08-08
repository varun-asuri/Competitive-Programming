from math import log10,pi,exp,floor
s=input()
l=len(s)
if l>3:
 a,b=-1,-1
 for n in range(1,369694):
  d=abs(floor(0.5*log10(2*pi*n)+n*log10(n/exp(1)))-l+1)
  if b==-1 or d<b:a,b=n,d
 print(a)
else:
 s,i=int(s),1
 while s!=1:i,s=i+1,s//(i+1)
 print(i)