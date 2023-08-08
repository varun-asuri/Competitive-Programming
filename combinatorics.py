n,h=input(),list(map(int,input().split()))
x,y,z,c=0,0,0,10**9+7
for i in h:
 if i==1:x+=1
 if i==2:y=(x+y+y)%c
 if i==3:z=(z+y)%c
print(z)