from bisect import bisect_right as br
p=int(input());s=[p+1]
for i in range(p):
 n=int(input());x=br(s,n)
 if x==len(s):s.append(n)
 else:s[x]=n
print(len(s))