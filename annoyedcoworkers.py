# “Author: Varun Asuri
# It is not ok to post my anonymized solution

import heapq # use a priority queue to sort which coworker to annoy next

read = input().split() # read input
numhelp, coworkers = int(read[0]), int(read[1]) # assign as the helps and coworkers

high = 0 # most annoyed coworker num
stack = [] # store all coworkers
for i in range(coworkers): # loop through all the coworker lines
    read = input().split() # read input
    curr, incr = int(read[0]), int(read[1]) # store as their current annoyance
    if curr > high: high = curr # if this coworker is more annoyed store how muc
    heapq.heappush(stack, (curr + incr, curr, incr) ) # push it into the queue which potential annoyance being the sorting number

for i in range(numhelp): # for the amount of times you need help
    nextval, curr, incr = heapq.heappop(stack) # pop the least potential annoyed coworker
    if nextval > high: high = nextval # if they are more annoyed than previous max store it
    heapq.heappush(stack, (nextval + incr, nextval, incr) ) # annoy them and push them back in with new potential

print(high) # print output