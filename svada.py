def v(g,t):return sum([(1+(t-m[0])//m[1])*(m[0]<=t) for m in g]) # function to return number of coconuts processed
t=int(input());P,S=[],[];l=o=0;h=a=t # read in time and define lists for both monkey types; define the lo and hi for binary search while creating a and o to hold the best option found
for i in range(int(input())):P.append(tuple(map(int,input().split()))) # read in all the monkey times for type 1
for i in range(int(input())):S.append(tuple(map(int,input().split()))) # read in all the monkey times for type 2
while l<=h: # while low is less than or equal to high
 m=(h+l)//2 # assign the new mid
 p,s=v(P,m),v(S,t-m) # calculate both coconut counts
 u=min(p,s) # find the minimum for actual processed
 if u>o:o=u;a=m # if its a better count then i store it
 if p>s:h=m-1 # if left is greater shift left
 if p<=s:l=m+1 # if right is greater shift right
print(a) # print result