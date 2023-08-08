g,p=range,input;l,n=list(map(int, p().split())),{};m,x=l[0],l[1];r=[set() for i in g(m)] # define the number of instruments and notes along with dictionaries and sets for access
for i in g(m): # for every instrument
 for v in p().split()[1:]:K=int(v);n[K]=n.get(K,[])+[i];r[i].add(K) # create a set of its playable notes then map backwards with a dictionary
k,s=list(map(int,p().split())),[[x+1]*m for j in g(x+1)];s[0]=[0]*m # read in all the notes and create a dp array to store least switches at each note
for i in g(x): # for every note
 for j in g(m): # for ever instrument
  if s[i][j]!=x+1: # if I have reached this location
   if k[i] in r[j]:s[i+1][j]=min(s[i+1][j],s[i][j]) # if I can play this note play and set the next on to no increase
   for M in n[k[i]]:s[i+1][M]=min(s[i+1][M],s[i][j]+1) # compute all the other instruments i can play it on and put those in the array with one switch
print(min(s[-1])) # print result