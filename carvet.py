# “Author: Varun Asuri
# It is ok to post my anonymized solution

import sys
sys.setrecursionlimit(2147483647) # avoid recursion depth max problem
m,n=tuple(map(int, input().split())) # read the m and n from the given input
c,d,g,w,p={},{},[],set(),[] # define the dictionaries, grid, visited set, and the solution list
def move(t): # recursion function named move
 v,f=g[t[0]][t[1]],[] # receive the car i am currently on top of and initialize a solution holder f
 if v==-1:return p[::] # return a copy of all the moves made before i change the list
 if v==-2 or v in w:return[] # if i run into a wall or re run into the same cars exit on fail
 w.add(v) # add this car to visited array
 a,b=c[v][0],c[v][-1] # store the two indices of the current car to make solutions easier
 if d[v]=='V': # if the car is a vertical moving one check the vertical movements
  if t==a and b[0]<m-1: # if i can move down move down
   p.append(v) # add it to the global path tracking list
   f=move((b[0]+1,a[1])) # make the move recursively and check it later
   p.pop() # pop it right off after processing
  elif t==b and a[0]>0: # if i can move up move up
   p.append(v)
   f=move((a[0]-1,a[1]))
   p.pop()
 else: # if the car is a horizontal moving one check the horizontal movements
  if t==a and b[1]<n-1: # if i can move right move right
   p.append(v)
   f=move((a[0], b[1]+1))
   p.pop()
  elif t==b and a[1]>0: # if i can move left move left
   p.append(v)
   f=move((a[0],a[1]-1))
   p.pop()
 return f # return the solution array empty or not to process outside
for i in range(m):g.append(list(map(int,input().split())))
for i in range(m): # for every index in the row count
 for j in range(n): # for every index in the column count
  v=g[i][j] # store the value of this given index for easier coding
  if v>=0: # for actual cars not walls and empty spots
   if v in d: # if the car has been seen before
    c[v].append((i,j)) # add in the new index to the cars list of spots
    if i==c[v][0][0]:d[v]='H' # if the horizontal indices are the same in this one as the previously found index of the car its horizontal
    else:d[v]='V' # if not its vertical
   else:c[v],d[v]=[(i,j)],'X' # if this is a new index for the car then add it in and establish the direction as a fill character
t=tuple(map(lambda y:int(y)-1,input().split()))
o=move(t)[::-1] # reverse the list to first to last moved cars
if o:print(' '.join([str(s) for s in o])) # if the list is larger than size 0 print it out
else:print('impossible') # if not then it means the problem is impossible