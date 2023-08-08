n,w,h=map(int,input().split());c,d=10**9+7,[[-1]*(n+1) for i in range(w+1)]
def a(t,r):
 if r<0:return 0
 if t>w:return 1
 if d[t][r]!=-1:return d[t][r]
 d[t][r]=sum([a(t+1,r-i) for i in range(h+1)])%c
 return d[t][r]
print((a(1,n)-(min(w*h,n)//w)-1+c)%c)