# “Author: Varun Asuri
# It is ok to post my anonymized solution

n,w,r,x=int(input()),list(map(int,input().split())),range,200 # define the number of fruit weights, the fruit weights, r as range for length, and the 200 cap
t=(2**(n-1))*sum(w) # find the maximum weight in the truck possible
for i in r(n): # loop through the range
 if w[i]<x:t-=w[i] # for every individual fruit if it is under 200 subtract it
 for j in r(i+1,n): # loop through the range after i
  if w[i]+w[j]<x:t-=w[i]+w[j] # for every pair of fruits if it is under 200 subtract it
  for k in r(j+1,n): # loop through the range after j
   if w[i]+w[j]+w[k]<x:t-=w[i]+w[j]+w[k] # for every triplet of fruits if it is under 200 subtract it
print(t) # the final answer removed of under 200 groupings