# “Author: Varun Asuri
# It is not ok to post my anonymized solution

import heapq, sys # import heapq for dfs and sys for maxsize
cases = int(input()) # obtain number of cases
for i in range(cases): # loop through each case
    line = input().split() # obtain the first two numbers of n and time
    n, time, buttons = int(line[0]), int(line[1]), list(map(int, input().split())) # read them in and the buttons
    closest, reach, stack = (0, sys.maxsize), {0:0}, [(0, 0)] # define best solution, previously checked set, and my queue
    while stack: # while there are things remaining in the queue
        num, val = heapq.heappop(stack) # pop from the queue
        if val == time: # if this is on the solution
            if val < closest[1] or val == closest[1] and num < closest[0]: # is it better than anything ive found
                closest = (num, val) # store it
        else:
            for button in buttons: # for every button on the microwave
                num2, val2 = num + 1, val + button # apply it
                if val2 > 3600: val2 = 3600 # if I go over an hour set to one hours
                if val2 > 0 and val2 <= 3600 and (val2 not in reach or reach[val2] > num2): # if this is above 0 and not previously reached or it is better than before
                    if val2 >= time and (val2 < closest[1] or val2 == closest[1] and num2 < closest[0]): # if it qualifies as a solution and is better than what ive found
                        closest = (num2, val2) # store it
                    heapq.heappush(stack, (num2, val2) ) # push this to the queue to analyze with the buttons after
                    reach[val2] = num2 # add it to the visited set
    print(closest[0], closest[1] - time) # by this point ive found the solution so output amount of buttons and time gone over