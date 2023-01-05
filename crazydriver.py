# “Author: Varun Asuri
# It is not ok to post my anonymized solution

stops = int(input()) # store the number of gates
costs = [int(c) for c in input().split()] #store all the costs between gates
times = [int(t) for t in input().split()] #store all the times to pass gates

time = 0 # starting time is 0
total = 0 #starting expenditure is 0
curr = costs[0] # cheapest current path is the first one
for i in range(stops-1): # until we pass all the stops
    time += 1 # increment time
    total += costs[i] # travel the next path forward
    while times[i+1] > time: # while we cannot cross this gate
        total += curr * 2 # keep going back and forth on the cheapest path
        time += 2 # increment time accordingly
    if i < stops-2 and costs[i+1] < curr: # if this path is cheaper and in bounds
        curr = costs[i+1] # its the new cheapest path

print(total) # print total expenditure