# “Author: Varun Asuri
# It is not ok to post my anonymized solution

import sys # import sys for sys.maxsize

testcases = int(input()) # read in number of testcases
for run in range(testcases): # for each testcase run my code on it

    count = int(input()) # read in the number of climbs
    climbs = [int(x) for x in input().split()] # read in all the climb distances from the next line
    total = sum(climbs) # the sum of all the climb distances

    if total % 2: # if the sum is odd, there is no way to brake them up into ups and downs to equal 0
        print("IMPOSSIBLE") # print impossible as asked
        continue # continue to the next test case

    moved = [[sys.maxsize for i in range(total + 1)] for j in range(count)] # storing heighest height reached in array with dimensions of climbs done and current height
    direc = [[0 for i in range(total + 1)] for j in range(count)] # storing direction last travelled in array with dimensions of climbs done and current height

    moved[0][climbs[0]] = climbs[0] # heightest height reached is the current one after going up
    direc[0][climbs[0]] = 1 # first direction is upward

    for i in range(1, count): # loops through the number of climbs doing each one
        for j in range(total + 1): # loops through all the heights
            if moved[i - 1][j] != sys.maxsize: # if a previous climb pattern reached here
                if j >= climbs[i] and moved[i][j - climbs[i]] > moved[i - 1][j]: # if i can travel downard and the height i get to is lower than the current maximum height reached
                    direc[i][j - climbs[i]] = -1 # go downward and store 
                    moved[i][j - climbs[i]] = moved[i - 1][j] # store the new maximum height reached
                temp = max(moved[i - 1][j], j + climbs[i]) # checking current height with maximum height reached up to now to get maximum
                if moved[i][j + climbs[i]] > temp: # if maximum height reached up to this height after i climbs is higher or unreached
                    direc[i][j + climbs[i]] = 1 # go up towards this location and store
                    moved[i][j + climbs[i]] = temp # restore the new maximum height

    if moved[count - 1][0] == sys.maxsize: # if i don't reach back to the street then i didnt succeed
        print("IMPOSSIBLE") # print impossible as asked
        continue # continue to the next test case

    x = 0 # variable to store the current height as a pointer
    ans = [""] * count # array to store output
    for i in reversed(range(count)): # start at the ending location
        if direc[i][x] == 1: # if the last travel was upward
            x -= climbs[i] # go down in height to the previous climb's height
            ans[i] = "U" # add a U for going up
        else:
            x += climbs[i] # go up in height to the previous climb's height
            ans[i] = "D" # add a D for going down
    print("".join(ans)) # print out all the U's and D's put together