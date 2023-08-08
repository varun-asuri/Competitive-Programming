from random import randrange as r
n,a,b=int(input()),input(),input()
v=[(r(0,9**6),r(0,9**6))for i in range(n)]
p,q=set(),set()
def f(c,m):
 t,l=0,[]
 for i in c:
  if i=='(':continue
  if i.isdigit():t=t*10+int(i);continue
  if t!=0:t=v[t-1];m.add(t);l.append(t);t=0
  if i==')':j,k=l.pop(),l.pop();t=(j[0]+k[0],j[1]+k[1]);t=t[0]%(9**6),t[1]%(9**6);m.add(t);l.append(t);t=0
f(a,p);f(b,q)
print(len(p.intersection(q)))