x=9**7;a,b,c=[0]*x,[0]*x,input;f=n=0
for m in c().split()[1:]:a[int(m)]=1
for m in c().split()[1:]:b[int(m)]=1
for i in range(x):
 if a[i]*(b[i]+(f<1)):f=1-b[i];n+=1
 elif b[i] and f>=0:f=-1;n+=1
print(n)